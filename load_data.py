import psycopg2
import pandas as pd
import sqlalchemy

df = pd.read_csv('data.csv')

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/nextia-test')
con = engine.connect()

print(engine.table_names())

table_name = 'app_bienesmodel'
df.to_sql(table_name, con, if_exists='replace', index=False)
