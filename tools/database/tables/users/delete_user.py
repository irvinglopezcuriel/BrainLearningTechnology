from werkzeug.exceptions import *
from tools.database.tables.users.check_if_user_exist import check_if_user_exist
from tools.database.tables.users.get_user_by_id import get_user_by_id
from tools.is_valid_uuid import is_valid_uuid

def delete_user(cur, id):
    if not is_valid_uuid(id):
        raise BadRequest("Invalid Id")
    if check_if_user_exist(cur, id):
        user = get_user_by_id(cur, id)
        if user[3] == "admin@blt.com":
            raise BadRequest("Cannot delete default admin user")
        else:
            commandCheckUser = """
                DELETE
                FROM public.users
                WHERE id = '{}'
            """.format(id)
            cur.execute(commandCheckUser)
    else:
        raise BadRequest("User does not exist")