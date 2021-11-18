import random
from datetime import datetime

from app.settings import db


class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    ticket_number = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    redeemed_at = db.Column(db.DateTime, onupdate=datetime.now(), nullable=True)
    event_id = db.Column(db.Integer,
                         db.ForeignKey('events.id'))  # TODO Make bigint to store hashed number instead of raw

    @staticmethod
    def generate_ticket_number():
        random_number_one = str(random.randint(1, 300))
        random_number_two = str(random.randint(1, 300))
        ticket_number_string = random_number_one + random_number_two
        ticket_number = ticket_number_string  # TODO Hash the number and store to avoid duplicates

        return ticket_number

    def __repr__(self) -> str:
        return 'Ticket>>> {self.ticket_number}'
