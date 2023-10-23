import uuid

def add_category(cur, name):
    user_uuid = uuid.uuid4()
    command = """
        INSERT INTO categories (id, name) VALUES ('{}', '{}')
    """.format(user_uuid, name)
    cur.execute(command)