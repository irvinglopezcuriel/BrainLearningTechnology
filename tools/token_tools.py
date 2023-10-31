import jwt
import os
import datetime

def create_token(user):
    payload = {
        "id": str(user[0]),
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=30)
    }
    return jwt.encode(payload=payload, key=os.getenv('SECRET'), algorithm="HS256")
