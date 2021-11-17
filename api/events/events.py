from flask import Blueprint, request

events = Blueprint("events", __name__, url_prefix="/api/v1/events")


@events.post('/add_event')
def add_event():
    """
    Endpoint to create events. Each event should have a
    Name, Date and initial number of tickets.
    """

    name = request.json['name']
    date = request.json['date']
    number_of_tickets = request.json['number_of_tickets']


@events.get('/check_event/<int:event_id>')
def event_status(event):
    """
    See the total number of tickets and how
    many have been redeemed.
    """
    event = event
    return {'event_name': 'will go here!', 'tickets': 123}


@events.post('/add_tickets/<int:event_id>')
def add_tickets(event):
    """
    Add more tickets to an event.
    """
    event = event
    number_of_tickets = date = request.json['number_of_tickets']

    return {'detail': 'success!'}






