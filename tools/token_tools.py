import jwt
import os

def create_token(user):
    return jwt.encode( payload={"id": str(user[0])}, key=os.getenv('SECRET'), algorithm="HS256")
