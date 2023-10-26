import uuid
import bcrypt
import re
from tools.logging import logger

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def add_user(cur, firstname, lastname, email, password, role):
    if (re.fullmatch(email_regex, email)):
        user_uuid = uuid.uuid4()
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        command = """
            INSERT INTO users (id, firstname, lastname, email, password, role, isActive) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', 'true')
        """.format(user_uuid, firstname, lastname, email, hashed_password.decode('ascii'), role)
        cur.execute(command)
    else:
        raise TypeError("Email invalid")