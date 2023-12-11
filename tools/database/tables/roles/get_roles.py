def get_roles(cur):
    command = """
        SELECT *
        FROM public.roles
    """
    cur.execute(command)
    result = cur.fetchall()
    
    return result