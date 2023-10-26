from tools.logging import logger
from tools.database.db_con import get_db_instance
from tools.database.tables.users.add_user import add_user
from tools.database.tables.roles.add_role import add_role
import psycopg2
import os

def check_if_table_exist(table_name, cur):
    command = """
        SELECT EXISTS (
            SELECT relname
            FROM pg_class
            WHERE relname = '{}'
        )
    """.format(table_name)
    cur.execute(command)
    result = cur.fetchone()[0]
    return result

def init_user_table(cur):
    # Check if the user table exist. If not, create it
    if not check_if_table_exist("users", cur):
        logger.info("CREATE USERS TABLE")
        command = """
            CREATE TABLE IF NOT EXISTS users(
                id uuid PRIMARY KEY NOT NULL UNIQUE,
                firstname varchar(24) NOT NULL,
                lastname varchar(24) NOT NULL,
                email varchar(50) NOT NULL UNIQUE,
                password varchar(255) NOT NULL,
                role uuid NOT NULL,
                FOREIGN KEY(role) REFERENCES roles(id),
                isActive boolean NOT NULL DEFAULT true
            )
        """
        cur.execute(command)
    # Check if the admin user exist. If not create it
    command = """
        SELECT EXISTS (
            SELECT email
            FROM public.users
            WHERE email = 'admin@blt.com'
        )
    """
    cur.execute(command)
    result = cur.fetchone()[0]
    if not result:
        logger.info("CREATE ADMIN USER")
        role_command = """
            SELECT *
            FROM public.roles
            WHERE name = 'admin'
        """
        cur.execute(role_command)
        role_id = cur.fetchone()[0]
        add_user(cur, "admin", "admin", "admin@blt.com", "admin123", role_id)
    
def init_roles_table(cur):
    # Check if the user table exist. If not, create it
    if not check_if_table_exist("roles", cur):
        logger.info("CREATE ROLES TABLE")
        command = """
            CREATE TABLE IF NOT EXISTS roles(
                id uuid PRIMARY KEY NOT NULL UNIQUE,
                name varchar(24) NOT NULL,
                levelOfAccess integer NOT NULL CHECK (levelOfAccess >= 0)
            )
        """
        cur.execute(command)
    # Check if the admin role exist. If not create it
    command = """
        SELECT EXISTS (
            SELECT name
            FROM public.roles
            WHERE name = 'admin'
        )
    """
    cur.execute(command)
    result = cur.fetchone()[0]
    if not result:
        logger.info("CREATE ADMIN ROLE")
        add_role(cur, "admin", 1)
    
    # Check if the user role exist. If not create it
    command = """
        SELECT EXISTS (
            SELECT name
            FROM public.roles
            WHERE name = 'user'
        )
    """
    cur.execute(command)
    result = cur.fetchone()[0]
    if not result:
        logger.info("CREATE USER ROLE")
        add_role(cur, "user",0)
        
def init_categories_table(cur):
    # Check if the categories table exist. If not, create it
    if not check_if_table_exist("categories", cur):
        logger.info("CREATE CATEGORIES TABLE")
        command = """
            CREATE TABLE IF NOT EXISTS categories(
                id uuid PRIMARY KEY NOT NULL UNIQUE,
                name varchar(64) NOT NULL
            )
        """
        cur.execute(command)
        
def init_subcategories_table(cur):
    # Check if the categories table exist. If not, create it
    if not check_if_table_exist("subcategories", cur):
        logger.info("CREATE SUBCATEGORIES TABLE")
        command = """
            CREATE TABLE IF NOT EXISTS subcategories(
                id uuid PRIMARY KEY NOT NULL UNIQUE,
                name varchar(64) NOT NULL
            )
        """
        cur.execute(command)
        
def init_content_table(cur):
    # Check if the categories table exist. If not, create it
    if not check_if_table_exist("contents", cur):
        logger.info("CREATE CONTENTS TABLE")
        command = """
            CREATE TABLE IF NOT EXISTS contents(
                id uuid PRIMARY KEY NOT NULL UNIQUE,
                name varchar(64) NOT NULL,
                path text NOT NULL,
                category uuid NOT NULL,
                FOREIGN KEY(category) REFERENCES categories(id),
                subcategory uuid NOT NULL,
                FOREIGN KEY(subcategory) REFERENCES subcategories(id),
                type varchar(24) NOT NULL
            )
        """
        cur.execute(command)
    
def init_database(cur):
    cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'blt'")
    exists = cur.fetchone()
    if not exists:
        cur.execute('CREATE DATABASE blt')

def init_db():
    logger.info("INIT DB")
    db = psycopg2.connect(host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASS'), port=os.getenv('DB_PORT'))
    db.autocommit = True
    cursor = db.cursor()
    init_database(cursor)
    db.close()
    db, cursor = get_db_instance()
    
    init_roles_table(cursor)
    init_user_table(cursor)
    init_categories_table(cursor)
    init_subcategories_table(cursor)
    init_content_table(cursor)
    
    db.commit()