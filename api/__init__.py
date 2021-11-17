import os
from flask import Flask

from api.events.events import events
from api.tickets.tickets import tickets


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(SECRET_KEY=os.environ.get('SECRET_KEY'))
    else:
        app.config.from_mapping(test_config)

    @app.get('/')
    def homepage():
        return {'detail': 'Welcome to ticket manager API! Please Visit /docs for endpoints.'}  # TODO add url to docs

    app.register_blueprint(events)
    app.register_blueprint(tickets)

    return app
