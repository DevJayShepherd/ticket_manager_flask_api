from flask import Blueprint

from app.models.ticket_model import Ticket
from app.settings import db

tickets = Blueprint("tickets", __name__, url_prefix="/app/v1/tickets")


@tickets.get('/redeem/<int:ticket_number>')
def redeem_ticket(ticket_number):
    """
    Redeem a ticket:
    """

    ticket = Ticket.query.filter_by(ticket_number=ticket_number).first()
    if not ticket:
        return {'detail': 'ticket not found, check number and try again.'}

    if ticket.status == 'redeemed':
        return {'detail': 'ticket already redeemed!'}

    ticket.status = 'redeemed'
    db.session.commit()

    return {'ticket_number': ticket.ticket_number, 'event': ticket.events.name, 'status': 'redeemed successfully!'}


@tickets.get('/check_ticket/<int:ticket_number>')
def check_ticket(ticket_number):
    """
    Check the status of a ticket.
    """

    ticket = Ticket.query.filter_by(ticket_number=ticket_number).first()
    if not ticket:
        return {'detail': 'ticket not found, check number and try again.'}

    return {'ticket_number': ticket.ticket_number, 'event': ticket.events.name, 'status': ticket.status}
