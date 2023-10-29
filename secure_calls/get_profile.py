from flask import request, g
from flask_json import json_response
from tools.database.tables.users.get_user_by_id import get_user_by_id
from tools.database.tables.roles.get_role_by_id import get_role_by_id
from werkzeug.exceptions import *

from tools.logging import logger

def handle_request():
    logger.debug("Get Profile Handle Request")

    userRole = get_role_by_id(g.cursor, g.user[5])
    
    result = {
        "id": g.user[0],
        "firstname": g.user[1],
        "lastname": g.user[1],
        "email": g.user[1],
        "role": {
            "id": userRole[0],
            "name": userRole[1],
            "levelOfAccess": userRole[2]
        }
    }
    
    return json_response(status_=200, user=result)
