from datetime import datetime

from api.core import db


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date)
    number_of_tickets = db.Column(db.Integer, nullable=False)
    tickets = db.relationship('Ticket', backref="events")

