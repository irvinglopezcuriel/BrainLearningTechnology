def get_user_by_id(cur, id):
    commandCheckUser = """
        SELECT *
        FROM public.users
        WHERE id = '{}' AND isactive = true
    """.format(id)
    cur.execute(commandCheckUser)
    result = cur.fetchone()
    if not result:
        raise TypeError("User does not exist")
    else:
        return result