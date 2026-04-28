import pandas as pd
import sqlite3
import re

data = ["player_data.csv", "performance_data.csv", 
        "league_data.csv", "team_data.csv", "team_player_data.csv"]

for file in data:
    table = re.match(".*?(?=_data.csv)", file).group()
    print(table)