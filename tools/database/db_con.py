import psycopg2
import os

def get_db():
    return psycopg2.connect(database="blt", host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASS'), port=os.getenv('DB_PORT'))

def get_db_instance():  
    db = get_db()
    cur = db.cursor()

    return db, cur
