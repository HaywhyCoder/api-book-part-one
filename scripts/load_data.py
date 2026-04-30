import pandas as pd
import sqlite3
import re
import os

data = os.listdir("data")

conn = sqlite3.connect('swc_database.db')
for file in data:
    path = os.path.join("data", file)
    table = re.match(".*?(?=_data.csv)", file).group()

    df = pd.read_csv(path)
    df.to_sql(table, conn, if_exists='replace', index=False)

conn.close()
