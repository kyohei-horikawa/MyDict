import sqlite3
from os.path import expanduser


def find(item):
    flag = True
    home = expanduser("~")
    conn = sqlite3.connect(f'{home}/dictionary.db')
    c = conn.cursor()
    c.execute('SELECT * FROM items')

    for element in c.fetchall():
        if element[1] == item:
            print(f'{element[1]}: {element[2]}\n')
            print(f'in {element[0]}')
            flag = False

    if flag:
        print(f'{item} is not in dictionary')

    conn.close()


def findInteractive():
    pass
