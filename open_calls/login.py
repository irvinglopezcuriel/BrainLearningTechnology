from flask import request, g
from flask_json import json_response
from tools.token_tools import create_token
from tools.database.tables.users.get_user import get_user
from werkzeug.exceptions import *

from tools.logging import logger

def handle_request():
    logger.debug("Login Handle Request")
    
    email = request.form.get('mail')
    password = request.form.get('password')
    
    print(email, password)
    
    if not email or not password:
        raise BadRequest("Invalid form data")
    
    user, role = get_user(g.cursor, str(email), str(password))

    return json_response(status_=200, token = str(create_token(user)), role = role[1])