import psycopg2
import pandas as pd
from sqlalchemy import create_engine

settingsdb = {
    'host': 'localhost',
    'port': '5432',
    'database': 'nextia-test',
    'user': 'postgres',
    'password': 'postgres'
}

engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{database}'.format(**settingsdb))

df = pd.read_csv('data.csv')

try:
    df.to_sql('app_bienesmodel', engine, if_exists='replace', index=False)
except:
    print('Error')
finally:
    engine.dispose()


