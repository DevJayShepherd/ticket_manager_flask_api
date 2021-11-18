from flask import Blueprint, request, jsonify
from flask_api import status

from app.models.event_model import Event
from app.models.ticket_model import Ticket
from app.settings import db

events = Blueprint("events", __name__, url_prefix="/app/v1/events")


@events.post('/add_event')
def add_event():
    """
    Endpoint to create events. Each event should have a
    Name, Date and initial number of tickets.
    """

    name = request.json['name']
    date = request.json['date']
    number_of_tickets = request.json['number_of_tickets']

    if Event.query.filter_by(name=name).first():
        return jsonify({
            'error': 'Event already exists'
        }), status.HTTP_409_CONFLICT

    event = Event(name=name, date=date, number_of_tickets=number_of_tickets)
    db.session.add(event)
    db.session.commit()

    for ticket in range(number_of_tickets):
        ticket_number = Ticket.generate_ticket_number()
        ticket = Ticket(ticket_number=ticket_number, status='available', event_id=event.id)
        db.session.add(ticket)
        db.session.commit()

    return jsonify({
        'id': event.id,
        'name': event.name,
        'date': event.date,
        'number_of_tickets': event.number_of_tickets,
    }), status.HTTP_201_CREATED


@events.get('/check_event/<int:event_id>')
def event_status(event_id):
    """
    See the total number of tickets and how
    many have been redeemed.
    """

    event = Event.query.filter_by(id=event_id).first()

    if not event:
        return {'detail': 'event not found, check id and try again.'}

    return {'event_name': event.name, 'date': event.date, 'tickets': event.number_of_tickets}


@events.post('/add_tickets/')
def add_tickets():
    """
    Add more tickets to an event.
    """
    event_name = request.json['event']
    number_of_tickets = request.json['number_of_tickets']

    event = Event.query.filter_by(name=event_name).first()
    if not event:
        return {'detail': 'event not found, check name and try again.'}

    new_ticket_amount = event.number_of_tickets + number_of_tickets
    event.number_of_tickets = new_ticket_amount
    db.session.commit()

    for ticket in range(number_of_tickets):
        ticket_number = Ticket.generate_ticket_number()
        ticket = Ticket(ticket_number=ticket_number, status='available', event_id=event.id)
        db.session.add(ticket)
        db.session.commit()

    return {'event': event.name, 'new_number_of_tickets': new_ticket_amount}
