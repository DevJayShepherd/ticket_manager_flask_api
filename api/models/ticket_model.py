import random
from datetime import datetime

from api.core import db


class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    ticket_number = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    redeemed_at = db.Column(db.DateTime, onupdate=datetime.now(), nullable=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    def generate_ticket_number(self):
        random_number_one = str(random.randint(1, 5000))
        random_number_two = str(random.randint(1, 5000))
        ticket_number_string = random_number_one + random_number_two
        ticket_number = hash(ticket_number_string)

        return ticket_number

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ticket_number = self.generate_ticket_number()

    def __repr__(self) -> str:
        return 'Ticket>>> {self.ticket_number}'




