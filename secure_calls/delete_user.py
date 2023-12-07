from flask import request, g
from flask_json import json_response
from tools.database.tables.users.delete_user import delete_user
from werkzeug.exceptions import *

from tools.logging import logger

def handle_request():
    logger.debug("DELETE delete user Handle Request")

    userId = request.form.get('userId')

    if userId:
        if g.userRole[2] != 1:
            raise Forbidden("Insufficient permission")
    else:
        userId = g.user[0]

    delete_user(g.cursor, userId)
    g.db.commit()

    return json_response(status_=200, data_={})
