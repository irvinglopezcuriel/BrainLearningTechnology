from flask import request, g
from flask_json import json_response
from tools.database.tables.users.add_user import add_user
from tools.database.tables.roles.get_role_by_name import get_role_by_name
from werkzeug.exceptions import *

from tools.logging import logger

def handle_request():
    logger.debug("Register Handle Request")

    firstname = request.form.get('firstname')
    lastname = request.form.get('firstname')
    email = request.form.get('email')
    password = request.form.get('password')

    if not firstname or not lastname or not email or not password:
        raise BadRequest("Invalid form data")

    role = get_role_by_name(g.cursor, "user")

    add_user(g.cursor, firstname, lastname, email, password, role[0])
    g.db.commit()
    
    return json_response(status_=200)
