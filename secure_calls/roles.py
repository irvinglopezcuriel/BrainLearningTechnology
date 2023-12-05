from flask import g, jsonify, make_response
from tools.database.tables.roles.get_roles import get_roles
from werkzeug.exceptions import *

from tools.logging import logger

def handle_request():
    logger.debug("GET get roles Handle Request")

    roles = get_roles(g.cursor)

    return make_response(jsonify(roles), 200)
