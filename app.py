from flask import Flask

app = Flask(__name__)


@app.get('/')
def homepage():
    return {'detail': 'Welcome to ticket manager API! Please Visit /docs for endpoints.'}  # TODO add url to docs
