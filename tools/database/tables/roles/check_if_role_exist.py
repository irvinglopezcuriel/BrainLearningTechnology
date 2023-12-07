from werkzeug.exceptions import *
from tools.is_valid_uuid import is_valid_uuid

def check_if_role_exist(cur, id):
    if not is_valid_uuid(id):
        raise BadRequest("Invalid Id")
    commandCheckRole = """
        SELECT EXISTS (
            SELECT id
            FROM public.roles
            WHERE id = '{}'
        )
    """.format(id)
    cur.execute(commandCheckRole)
    result = cur.fetchone()[0]
    return result