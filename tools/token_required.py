import jwt
from functools import wraps
from flask import request, g
from flask_json import json_response

from tools.logging import logger

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        secrets = get_secrets()
        auth_headers = request.headers.get('Authorization', '').split(':')

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return json_response(status_=401 ,message=invalid_msg)

        try:
            token = auth_headers[1]
            logger.debug("Got token")
            data = jwt.decode(token,  secrets['JWT'], algorithms=["HS256"])
            #set global jwt_data
            g.jwt_data = data
            return f( *args, **kwargs)
        except jwt.ExpiredSignatureError:
             return json_response(status_=401 ,message=expired_msg) # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            logger.debug(e)
            return json_response(status_=401 ,message=expired_msg)

    return _verify
