import os
from flask import Flask
from flask_migrate import Migrate
from app.settings import db

from app.routes.events import events
from app.routes.tickets import tickets

from app.models.ticket_model import Ticket
from app.models.event_model import Event

from app.settings import DATABASE_URL

migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(SECRET_KEY=os.environ.get('SECRET_KEY'),
                                SQLALCHEMY_DATABASE_URI=DATABASE_URL, )
    else:
        app.config.from_mapping(test_config)

    @app.get('/')
    def homepage():
        return {'detail': 'Welcome to ticket manager API! Please Visit /docs for endpoints.'}  # TODO add url to docs

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(events)
    app.register_blueprint(tickets)

    return app
