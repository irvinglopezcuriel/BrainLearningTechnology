from werkzeug.exceptions import *
from tools.is_valid_uuid import is_valid_uuid

def delete_subcategory(cur, id):
    if not is_valid_uuid(id):
        raise BadRequest("Invalid Id")
    commandCheckUser = """
        DELETE
        FROM public.subcategories
        WHERE id = '{}'
    """.format(id)
    cur.execute(commandCheckUser)