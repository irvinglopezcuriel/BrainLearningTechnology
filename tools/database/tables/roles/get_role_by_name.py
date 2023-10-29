from werkzeug.exceptions import BadRequest

def get_role_by_name(cur, name):
    command = """
        SELECT *
        FROM public.roles
        WHERE name = '{}'
    """.format(name)
    cur.execute(command)
    result = cur.fetchone()
    if not result:
        raise BadRequest("Role does not exist")
    else:
        return result