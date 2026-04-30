import sqlite3

def init_db():
    conn = sqlite3.connect('swc_database.db')
    cursor = conn.cursor()
    
    # Enable foreign key support
    cursor.execute("PRAGMA foreign_keys = ON;")

    print("Creating tables...")

    # 1. Create Player table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS player (
            player_id INTEGER NOT NULL,
            gsis_id VARCHAR,
            first_name VARCHAR NOT NULL,
            last_name VARCHAR NOT NULL,
            position VARCHAR NOT NULL,
            last_changed_date DATE NOT NULL,
            PRIMARY KEY (player_id)
            )
''')

    # 2. Create performance table     
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS performance (
            performance_id INTEGER NOT NULL,
            week_number VARCHAR NOT NULL,
            fantasy_points FLOAT NOT NULL,
            player_id INTEGER NOT NULL,
            last_changed_date DATE NOT NULL,
            PRIMARY KEY (performance_id)
            FOREIGN KEY(player_id) REFERENCES player (player_id)
            )
''')

    # 3. Create league table 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS league (
            league_id INTEGER NOT NULL,
            league_name VARCHAR NOT NULL,
            scoring_type VARCHAR NOT NULL,
            last_changed_date DATE NOT NULL,
            PRIMARY KEY (league_id)
            )
''')
    
    # 4. Create team table 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS team (
            team_id INTEGER NOT NULL,
            team_name VARCHAR NOT NULL,
            league_id INTEGER NOT NULL,
            last_changed_date DATE NOT NULL,
            PRIMARY KEY (team_id)
            FOREIGN KEY(league_id) REFERENCES league (league_id)
            )
''')

    # 5. Create team_player table 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS team_player (
            team_id INTEGER NOT NULL,
            player_id INTEGER NOT NULL,
            last_changed_date DATE NOT NULL,
            PRIMARY KEY (team_id, player_id)
            FOREIGN KEY(team_id) REFERENCES team (team_id)
            FOREIGN KEY(player_id) REFERENCES player (player_id)
            )
''')
    
    conn.commit()
    conn.close()
    print("Database 'swc_database.db' initialized successfully.")

if __name__ == "__main__":
    init_db()