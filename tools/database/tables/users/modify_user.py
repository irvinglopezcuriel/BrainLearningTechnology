import uuid
import bcrypt
import re
from werkzeug.exceptions import *
from tools.database.tables.users.get_user_by_id import get_user_by_id
from tools.database.tables.roles.check_if_role_exist import check_if_role_exist
import json

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def modify_user(cur, userId, firstname, lastname, email, password, role, isActive):
    if email:
        if re.fullmatch(email_regex, email) == None:
            raise BadRequest("Invalid email format")
    hashed_password = ""
    
    if password:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    if role:
        if not check_if_role_exist(cur, role):
            raise BadRequest("Invalid role id")
    
    userData = get_user_by_id(cur, userId)
    infos = {
        "firstname": firstname if firstname else userData[1],
        "lastname": lastname if lastname else userData[2],
        "email": email if email else userData[3],
        "password": hashed_password if password else userData[4],
        "role": role if role else userData[5],
        "isActive": isActive if isActive else userData[6]
    }
    command = """
        UPDATE users
        SET firstname = '{}',
            lastname = '{}',
            email = '{}',
            password = '{}',
            role = '{}',
            isActive = '{}'
        WHERE id = '{}'
    """.format(infos["firstname"], infos["lastname"], infos["email"], infos['password'], infos['role'], infos['isActive'], userId)
    cur.execute(command)