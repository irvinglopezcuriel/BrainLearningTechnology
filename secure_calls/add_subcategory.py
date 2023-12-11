from flask import request, g
from flask_json import json_response
from tools.database.tables.subcategories.add_subcategory import add_subcategory
from werkzeug.exceptions import *

from tools.logging import logger

def handle_request():
    logger.debug("POST add subcategory Handle Request")

    name = request.form.get('name')

    if not name:
        raise BadRequest("Bad Request")

    add_subcategory(g.cursor, name)
    g.db.commit()

    return json_response(status_=200, data_={})
