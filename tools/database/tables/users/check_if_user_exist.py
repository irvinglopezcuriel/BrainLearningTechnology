from werkzeug.exceptions import *
from tools.is_valid_uuid import is_valid_uuid

def check_if_user_exist(cur, id):
    if not is_valid_uuid(id):
        raise BadRequest("Invalid Id")
    commandCheckUser = """
        SELECT EXISTS (
            SELECT id
            FROM public.users
            WHERE id = '{}'
        )
    """.format(id)
    cur.execute(commandCheckUser)
    result = cur.fetchone()[0]
    return result