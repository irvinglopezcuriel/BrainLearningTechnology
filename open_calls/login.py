from flask import request, g
from flask_json import json_response
from tools.token_tools import create_token
from tools.database.tables.users.get_user import get_user

from tools.logging import logger

def handle_request():
    logger.debug("Login Handle Request")
    
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        user, role = get_user(g.cursor, email, password)
        
        return json_response( token = create_token(user), role = role[1])
    except Exception as err:
        return json_response(status_=400, data=err)