from flask import g, jsonify, make_response
from tools.database.tables.users.get_users import get_users
from werkzeug.exceptions import *

from tools.logging import logger

def handle_request():
    logger.debug("GET get users Handle Request")

    users = get_users(g.cursor)

    return make_response(jsonify(users), 200)
