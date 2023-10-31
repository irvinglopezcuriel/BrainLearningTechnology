from flask import request, g
from flask_json import json_response
from tools.database.tables.users.delete_user import delete_user
from tools.database.tables.roles.get_role_by_id import get_role_by_id
from werkzeug.exceptions import *

from tools.logging import logger

def handle_request():
    logger.debug("DELETE delete user Handle Request")

    userId = request.form.get('id')

    if userId:
        userRole = get_role_by_id(g.cursor, g.user[5])
        if int(userRole[2]) < 1:
            raise Forbidden("Insufficient permission")
    else:
        userId = g.user[0]

    delete_user(g.cursor, userId)

    return json_response(status_=200)
