import psycopg2
import pandas as pd

settingsdb = {
    'host': 'localhost',
    'port': '5432',
    'database': 'nextia-test',
    'user': 'postgres',
    'password': 'postgres'
}

def connect_db():
    try:
        conn = psycopg2.connect(**settingsdb)
        return conn
    except:
        print("No puedo conectarme a la base de datos. ")

