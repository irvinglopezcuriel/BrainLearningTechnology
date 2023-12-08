import uuid

def add_subcategory(cur, name):
    user_uuid = uuid.uuid4()
    command = """
        INSERT INTO subcategories (id, name) VALUES ('{}', '{}')
    """.format(user_uuid, name)
    cur.execute(command)