def get_categories(cur):
    commandCheckUser = """
        SELECT id, name
        FROM public.categories
    """
    
    cur.execute(commandCheckUser)
    result = cur.fetchall()
    
    return result