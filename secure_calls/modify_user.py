from flask import request, g
from flask_json import json_response
from tools.database.tables.users.modify_user import modify_user
from werkzeug.exceptions import *

from tools.logging import logger

def handle_request():
    logger.debug("POST modify user Handle Request")

    userId = request.form.get('userId')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')

    if userId:
        if g.userRole[2] != 1:
            raise Forbidden("Insufficient permission")
    else:
        userId = g.user[0]

    modify_user(g.cursor, userId, firstname, lastname, None, None, None, None)
    g.db.commit()

    return json_response(status_=200, data_={})
