from flask import request
from flask_json import json_response
from tools.token_tools import create_token

from tools.logging import logger

def handle_request():
    logger.debug("Login Handle Request")
    #use data here to auth the user

    password_from_user_form = request.form['password']
    user = {
            "sub" : request.form['firstname'] #sub is used by pyJwt as the owner of the token
            }
    if not user:
        return json_response(status_ = 401, message = 'Invalid credentials', authenticated = False )

    return json_response( token = create_token(user) , authenticated = True)
