from flask import g, jsonify, make_response
from flask_json import json_response
from tools.database.tables.subcategories.get_subcategories import get_subcategories
from werkzeug.exceptions import *

from tools.logging import logger

def handle_request():
    logger.debug("Get SubCategories Handle Request")

    categories = get_subcategories(g.cursor)
    
    return make_response(jsonify(categories), 200)
