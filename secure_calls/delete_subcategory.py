from flask import request, g
from flask_json import json_response
from tools.database.tables.categories.delete_subcategory import delete_subcategory
from werkzeug.exceptions import *

from tools.logging import logger

def handle_request():
    logger.debug("DELETE delte subcategory Handle Request")

    categoryId = request.form.get('categoryId')

    if not categoryId:
        raise BadRequest("Bad Request")

    delete_subcategory(g.cursor, categoryId)
    g.db.commit()

    return json_response(status_=200, data_={})
