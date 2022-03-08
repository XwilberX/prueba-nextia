import psycopg2
import pandas as pd
import datetime as dt

settingsdb = {
    'host': 'localhost',
    'port': '5432',
    'database': 'nextia-test',
    'user': 'postgres',
    'password': 'wil99'
}

df = pd.read_csv('data.csv')

conn = psycopg2.connect(**settingsdb)
cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute(f"INSERT INTO app_bienesmodel (id, created_at, updated_at, article, description, id_user_id) VALUES ({row['id']}, '{dt.datetime.now()}', '{dt.datetime.now()}', '{row['articulo']}', '{row['descripcion']}', {row['id_user_id']})")
    conn.commit()

cursor.close()
conn.close()