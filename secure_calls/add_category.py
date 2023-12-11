from flask import request, g
from flask_json import json_response
from tools.database.tables.categories.add_category import add_category
from werkzeug.exceptions import *

from tools.logging import logger

def handle_request():
    logger.debug("POST add category Handle Request")

    name = request.form.get('name')

    if not name:
        raise BadRequest("Bad Request")

    add_category(g.cursor, name)
    g.db.commit()

    return json_response(status_=200, data_={})
