from werkzeug.exceptions import BadRequest
from tools.is_valid_uuid import is_valid_uuid

def get_role_by_id(cur, id):
    if not is_valid_uuid(id):
        raise BadRequest("Invalid Id")
    command = """
        SELECT *
        FROM public.roles
        WHERE id = '{}'
    """.format(id)
    cur.execute(command)
    result = cur.fetchone()
    if not result:
        raise BadRequest("Role does not exist")
    else:
        return result