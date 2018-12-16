import psycopg2
import os

url ="dbname='ireporter' host='localhost' port='5432' user='postgres' password='pycoders'"
def connection(url):
    conn = psycopg2.connect(url)
    return conn


def init_db():
    conn = connection(url)
    return conn


def init_test_db():
    conn = connection(test_url)
    return conn  


def create_tables():
    users = """CREATE TABLE IF NOT EXISTS users(
    id serial PRIMARY KEY NOT NULL,
    firstname VARCHAR(191) NOT NULL,
    lastname VARCHAR(130) NOT NULL,
    email VARCHAR(130) NOT NULL,
    phonenumber VARCHAR(120) NOT NULL,
    username VARCHAR(140) NOT NULL,
    password VARCHAR(140)NOT NULL,
    registered timestamp with time zone DEFAULT('now'::text)::date NOT NULL,
    isadmin VARCHAR(130)  DEFAULT 'false' NOT NULL)"""

    incidents = """CREATE TABLE IF NOT EXISTS incidents(
            incident_id serial PRIMARY KEY NOT NULL,
            created_on timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
            created_by VARCHAR(150)  NOT NULL,
            title VARCHAR(140),
            comment VARCHAR(130),
            instance_type VARCHAR(100) NOT NULL,
            location VARCHAR(120),
            status VARCHAR(100) DEFAULT 'draft' NOT NULL,
            images bytea,
            videos bytea
            )"""
    queries = [users, incidents]

    conn = connection(url)
    cur = conn.cursor()
    for query in queries:
        cur.execute(query)
    conn.commit()
    return queries


def admin():
        conn = connection(url)
        cur = conn.cursor()

        firstname = 'jane'
        lastname = 'ranger'
        email = 'admin@gmail.com'
        phonenumber = '0778096758'
        username = 'admin'
        password = 'admin'
        isadmin = True

        sql = "SELECT * FROM users WHERE username = %s"
        cur.execute(sql, (username,))
        data = cur.fetchone()

        if not data:
            sql = """INSERT INTO users(firstname, lastname, email, phonenumber, username, password, isadmin)\
                        VALUES(%s, %s, %s, %s, %s, %s, %s)"""
            cur.execute(sql, (firstname, lastname, email, phonenumber, username, password, isadmin))
            conn.commit()


def tearDown():
    pass
