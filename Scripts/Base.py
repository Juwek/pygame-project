import sqlite3
from constants import BASE

values = ['coins']


def create_base():
    base = sqlite3.connect(BASE)
    cur = base.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Data (
    id INTEGER PRIMARY KEY,
    coins INTEGER
    )
    ''')
    base.commit()
    cur.execute('''
    INSERT INTO Data (coins) VALUES (0)
    ''')
    base.commit()
    base.close()


def get_data():
    base = sqlite3.connect(BASE)
    cur = base.cursor()
    data = cur.execute('''
    SELECT * FROM Data
    ''').fetchall()
    base.close()
    return data


def set_data(arg, value):
    base = sqlite3.connect(BASE)
    cur = base.cursor()
    cur.execute('''
    UPDATE Data SET ? = ?
    ''', (str(arg), str(value)))
    base.close()