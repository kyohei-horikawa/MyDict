import sqlite3
from os.path import expanduser
import datetime


def add():
    categories = []
    dt_now = datetime.datetime.now()

    timeStamp = dt_now.strftime('%Y/%m/%d %H:%M:%S')

    home = expanduser("~")
    conn = sqlite3.connect(f'{home}/dictionary.db')
    c = conn.cursor()

    for row in c.execute('SELECT * FROM items'):
        if row[0] not in categories:
            categories.append(row[0])
    categories.append('new')

    for i, category in enumerate(categories):
        print(f'{i} {category}')

    select = int(input('\nselect one number above list: '))

    print()

    if categories[select] == 'new':
        category = input('category: ')
    else:
        category = categories[select]

    name = input('name: ')
    description = input('description: ')

    c.execute(f"INSERT INTO items VALUES ('{category}', '{name}', '{description}', '{timeStamp}')")

    conn.commit()
    conn.close()
