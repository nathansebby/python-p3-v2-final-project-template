import sqlite3

class Team:
    def __init__(self, id=None, name='', city='', mascot=''):
        self.id = id
        self.name = name
        self.city = city
        self.mascot = mascot

    @staticmethod
    def create_table():
        conn = sqlite3.connect('db/team_data.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS teams (
                id INTEGER PRIMARY KEY,
                name TEXT,
                city TEXT,
                mascot TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect('db/team_data.db')
        c = conn.cursor()
        if self.id:
            c.execute('UPDATE teams SET name=?, city=?, mascot=? WHERE id=?', 
                      (self.name, self.city, self.mascot, self.id))
        else:
            c.execute('INSERT INTO teams (name, city, mascot) VALUES (?, ?, ?)', 
                      (self.name, self.city, self.mascot))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('db/team_data.db')
        c = conn.cursor()
        c.execute('SELECT * FROM teams')
        teams = c.fetchall()
        conn.close()
        return teams

    @staticmethod
    def find_by_id(team_id):
        conn = sqlite3.connect('db/team_data.db')
        c = conn.cursor()
        c.execute('SELECT * FROM teams WHERE id=?', (team_id,))
        team = c.fetchone()
        conn.close()
        return team

    @staticmethod
    def delete(team_id):
        conn = sqlite3.connect('db/team_data.db')
        c = conn.cursor()
        c.execute('DELETE FROM teams WHERE id=?', (team_id,))
        conn.commit()
        conn.close()

class Jersey:
    def __init__(self, id=None, player_name='', number=0, size='', color='', team_id=None):
        self.id = id
        self.player_name = player_name
        self.number = number
        self.size = size
        self.color = color
        self.team_id = team_id

    @staticmethod
    def create_table():
        conn = sqlite3.connect('db/team_data.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS jerseys (
                id INTEGER PRIMARY KEY,
                player_name ,
                number INTEGER,
                size TEXT,
                color TEXT,
                team_id INTEGER,
                FOREIGN KEY (team_id) REFERENCES teams(id)
            )
        ''')
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect('db/team_data.db')
        c = conn.cursor()
        if self.id:
            c.execute('UPDATE jerseys SET player_name=?, number=?, size=?, color=?, team_id=? WHERE id=?', 
                      (self.player_name, self.number, self.size, self.color, self.team_id, self.id))
        else:
            c.execute('INSERT INTO jerseys (player_name, number, size, color, team_id) VALUES (?, ?, ?, ?, ?)', 
                      (self.player_name, self.number, self.size, self.color, self.team_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('db/team_data.db')
        c = conn.cursor()
        c.execute('SELECT * FROM jerseys')
        jerseys = c.fetchall()
        conn.close()
        return jerseys

    @staticmethod
    def find_by_id(jersey_id):
        conn = sqlite3.connect('db/team_data.db')
        c = conn.cursor()
        c.execute('SELECT * FROM jerseys WHERE id=?', (jersey_id,))
        jersey = c.fetchone()
        conn.close()
        return jersey

    @staticmethod
    def delete(jersey_id):
        conn = sqlite3.connect('db/team_data.db')
        c = conn.cursor()
        c.execute('DELETE FROM jerseys WHERE id=?', (jersey_id,))
        conn.commit()
        conn.close()
