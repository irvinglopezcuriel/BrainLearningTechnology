from flask import g, jsonify, make_response
from flask_json import json_response
from tools.database.tables.categories.get_categories import get_categories
from werkzeug.exceptions import *

from tools.logging import logger

def handle_request():
    logger.debug("Get Categories Handle Request")

    categories = get_categories(g.cursor)
    
    return make_response(jsonify(categories), 200)
