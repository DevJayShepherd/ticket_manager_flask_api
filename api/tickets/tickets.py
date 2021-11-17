from flask import Blueprint, request

tickets = Blueprint("tickets", __name__, url_prefix="/api/v1/tickets")


@tickets.get('/redeem/<int:ticket_number>')
def redeem_ticket(ticket_number):
    """
    Redeem a ticket:
    """

    ticket = ticket_number

    return {'detail': 'success'}


@tickets.get('/check_ticket/<int:ticket_number>')
def check_ticket(ticket_number):
    """
    Check the status of a ticket.
    """

    ticket = ticket_number

    return {'status': 'success'}

