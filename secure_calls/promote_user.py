from flask import request, g
from flask_json import json_response
from tools.database.tables.users.modify_user import modify_user
from tools.database.tables.users.check_if_user_exist import check_if_user_exist
from tools.database.tables.roles.get_role_by_id import get_role_by_id
from werkzeug.exceptions import *

from tools.logging import logger

def handle_request():
    logger.debug("POST Promote User Handle Request")
    
    if g.userRole[2] != 1:
        raise Forbidden("Insufficient permission")
    else:
        
        userId = request.form.get('userId')
        roleId = request.form.get('roleId')
        
        if not userId or not roleId:
            raise BadRequest('Invalid request')

        if not check_if_user_exist(g.cursor, userId):
            raise BadRequest('Invalid request')

        modify_user(g.cursor, userId, None, None, None, None, roleId, None)
        
        g.db.commit()
        
        return json_response(status_=200, data_={})
