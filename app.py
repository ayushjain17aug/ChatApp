#!/bin/env python
import sys
from flask import Flask
from flask_socketio import SocketIO
from flask import Blueprint


socketio = SocketIO()
main_blueprint = Blueprint('main', __name__)

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app

app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app)
