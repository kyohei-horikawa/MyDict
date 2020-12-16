import sqlite3
import os
from os.path import expanduser


def initialize():
    home = expanduser("~")

    if not ('dictionary.db' in os.listdir(home)):
        conn = sqlite3.connect(f'{home}/.dictionary.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE items(category text, name text, description text, date text)''')
        conn.close()

    else:
        print('your initialize had been already done')
