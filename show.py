import sqlite3
from os.path import expanduser


def showAllCategories():
    categories = []

    home = expanduser("~")
    conn = sqlite3.connect(f'{home}/dictionary.db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM items'):
        if row[0] not in categories:
            categories.append(row[0])

    print(f'You have {len(categories)} categories.\n\n')

    for category in categories:
        print(f'* {category}')

    conn.close()


def showItemsInCategory(category):
    items = []

    home = expanduser("~")
    conn = sqlite3.connect(f'{home}/dictionary.db')
    c = conn.cursor()
    c.execute('SELECT * FROM items')

    for element in c.fetchall():
        if element[0] == category:
            items.append(element[1])

    print(f'{len(items)} items are in {category} category\n\n')

    for item in items:
        print(f'* {item}')

    conn.close()


def showItem(category, name):
    home = expanduser("~")
    conn = sqlite3.connect(f'{home}/dictionary.db')
    c = conn.cursor()
    c.execute('SELECT * FROM items')

    for element in c.fetchall():
        if element[0] == category:
            if element[1] == name:
                print(f'{name}: {element[2]}')

    conn.close()


def showAll():
    categories = []

    home = expanduser("~")
    conn = sqlite3.connect(f'{home}/dictionary.db')
    c = conn.cursor()
    c.execute('SELECT * FROM items')

    for element in c.fetchall():
        if element[0] not in categories:
            categories.append(element[0])

    for category in categories:
        print(category)
        c.execute('SELECT * FROM items')
        for element in c.fetchall():
            if element[0] == category:
                print(f'    {element[1]}')

    conn.close()
