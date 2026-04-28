import pandas as pd
import re
import sqlite3

data = ["player_data.csv", "performance_data.csv", 
        "league_data.csv", "team_data.csv", "team_player_data.csv"]

conn = sqlite3.connect('swc_database.db')
for file in data:
    path = "data\\" + file 
    table = re.match(".*?(?=_data.csv)", file).group()

    df = pd.read_csv(path)
    df.to_sql(table, conn, if_exists='append', index=False)

conn.close()
