from flask import Blueprint

main = Blueprint('main', __name__)

from chat.main import routes, events
