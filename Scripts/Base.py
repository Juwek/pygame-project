import sqlite3
from constants import BASE

data_dict = {
    'coins': None,
    'maps': None
}


def create_base():
    base = sqlite3.connect(BASE)
    cur = base.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Data (
    id INTEGER PRIMARY KEY,
    coins INTEGER,
    maps TEXT
    )
    ''')
    base.commit()
    cur.execute('''
    INSERT INTO Data (coins, maps) VALUES (0, "1 0")
    ''')
    base.commit()
    base.close()


def get_data():
    base = sqlite3.connect(BASE)
    cur = base.cursor()
    data = cur.execute('''
    SELECT * FROM Data
    ''').fetchall()
    for i in enumerate(data_dict):
        data_dict[i[1]] = data[0][i[0] + 1]
    base.close()
    return data_dict


def set_data(arg, value):
    base = sqlite3.connect(BASE)
    cur = base.cursor()
    cur.execute(f'''
    UPDATE Data SET {arg} = ?
    ''', (str(value),))
    base.commit()
    base.close()