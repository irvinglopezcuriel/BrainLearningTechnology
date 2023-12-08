import uuid

def add_role(cur, name, level_of_access):
    user_uuid = uuid.uuid4()
    command = """
        INSERT INTO roles (id, name, levelOfAccess) VALUES ('{}', '{}', '{}')
    """.format(user_uuid, name, level_of_access)
    cur.execute(command)