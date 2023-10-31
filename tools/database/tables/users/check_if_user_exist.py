from werkzeug.exceptions import *

def check_if_user_exist(cur, id):
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