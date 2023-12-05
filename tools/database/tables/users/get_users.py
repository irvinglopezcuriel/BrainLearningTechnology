from tools.database.tables.roles.get_role_by_id import get_role_by_id

def get_users(cur):
    commandCheckUser = """
        SELECT id, firstname, lastname, email, role, isActive
        FROM public.users
    """
    
    cur.execute(commandCheckUser)
    result = cur.fetchall()
    result2 = []
    for user in result:
        user = list(user)
        role = list(get_role_by_id(cur, str(user[4])))
        user[4] = role[1]
        result2.append(user)
    
    return result2