from werkzeug.exceptions import *
from tools.is_valid_uuid import is_valid_uuid

def get_user_by_id(cur, id):
    if not is_valid_uuid(id):
        raise BadRequest("Invalid Id")
    commandCheckUser = """
        SELECT *
        FROM public.users
        WHERE id = '{}' AND isactive = true
    """.format(id)
    cur.execute(commandCheckUser)
    result = cur.fetchone()
    if not result:
        raise BadRequest("User does not exist")
    else:
        return result