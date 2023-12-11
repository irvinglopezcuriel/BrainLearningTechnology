from werkzeug.exceptions import *
from tools.is_valid_uuid import is_valid_uuid

def delete_category(cur, id):
    if not is_valid_uuid(id):
        raise BadRequest("Invalid Id")
    commandCheckUser = """
        DELETE
        FROM public.categories
        WHERE id = '{}'
    """.format(id)
    cur.execute(commandCheckUser)