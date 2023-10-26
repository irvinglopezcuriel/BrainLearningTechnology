import uuid

def add_content(cur, name, path, category, subcategory, type):
    user_uuid = uuid.uuid4()
    command = """
        INSERT INTO contents (id, name, path, category, subcategory, type) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')
    """.format(user_uuid, name, path, category, subcategory, type)
    cur.execute(command)