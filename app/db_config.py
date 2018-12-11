import psycopg2
import os

url = os.getenv('DATABASE_URL')
test_url = os.getenv('TESTDATABASE_URL')


def connection(url):
    conn = psycopg2.connect(url)
    return conn


def init_db():
    conn = connection(url)
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

    queries = [users]

    conn = connection(url)
    cur = conn.cursor()
    for query in queries:
        cur.execute(query)
    conn.commit()
    return queries


def destroy_table():
    pass
