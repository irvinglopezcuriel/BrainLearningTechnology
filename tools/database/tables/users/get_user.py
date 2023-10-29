import bcrypt
import re
from werkzeug.exceptions import BadRequest

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def get_user(cur, email, password):
    if (re.fullmatch(email_regex, email)):
        commandCheckUser = """
            SELECT *
            FROM public.users
            WHERE email = '{}' AND isactive = true
        """.format(email)
        cur.execute(commandCheckUser)
        result = cur.fetchone()
        if not result:
            raise BadRequest("User or password invalid")
        else:
            checkPassword = bcrypt.checkpw(password.encode('utf-8'), result[4].encode('utf-8'))
            if not checkPassword:
                raise BadRequest("User or password invalid")
            else:
                commandGetRole = """
                    SELECT *
                    FROM public.roles
                    WHERE id = '{}'
                """.format(result[5])
                cur.execute(commandGetRole)
                resultRole = cur.fetchone()
                return result, resultRole
    else:
        raise BadRequest("Invalid email format")
