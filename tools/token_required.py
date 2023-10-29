import jwt
from functools import wraps
from flask import request, g
from flask_json import json_response
import os
from tools.database.tables.users.get_user_by_id import get_user_by_id
from tools.database.db_con import get_db_instance

from tools.logging import logger

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        token = request.headers.get('Authorization', '')

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
        }

        if not token:
            return json_response(status_=401 ,message=invalid_msg)

        try:
            data = jwt.decode(token, key=os.getenv('SECRET'), algorithms=["HS256"])
            logger.info(data)
            if 'db' not in g:
                g.db, g.cursor = get_db_instance()
            g.user = get_user_by_id(g.cursor, data['id'])
            return f( *args, **kwargs)
        except jwt.ExpiredSignatureError:
             return json_response(status_=401 ,message=expired_msg) # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            logger.debug(e)
            return json_response(status_=401 ,message=expired_msg)

    return _verify
