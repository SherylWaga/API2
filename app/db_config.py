import psycopg2
import os

url="dbname='ireporter' host='localhost' port='5432' user='postgres' password='pycoders'"

def connection (url):
    conn=psycopg2.connect(url)
    return conn
def init_db():
    conn=connection(url)
    return conn
def create_tables():
    conn=connection(url)
    cur=conn.cursor()
    queries=tables() 
    for query in queries:
        cur.execute(query)
    conn.commit()

def destroy_table():
    pass

def tables():
    users = """CREATE TABLE IF NOT EXISTS users(
    id serial PRIMARY KEY NOT NULL,
    firstname char(30) NOT NULL,
    lastname char(30)NOT NULL,
    email char(30) NOT NULL,
    phonenumber char (20) NOT NULL,
    username char(40) NOT NULL,
    password char(40)NOT NULL,
    registered timestamp with time zone DEFAULT('now'::text)::date NOT NULL,
    isadmin char(40)  DEFAULT 'false' NOT NULL)"""

    queries=[users]

    return queries