from werkzeug.exceptions import BadRequest

def get_role_by_id(cur, id):
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