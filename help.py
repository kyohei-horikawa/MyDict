def help():
    print('Dictionary only for you\n')

    print('usage: main.py [-h help] [-s show] [-a add] [init]\n')
    string = '''optional arguments:

  init                                 Initialize your dictionary
  -h, help                             Show this help message

  -s, show                             Show all categories
  -s, show all                         Show all items
  -s, show <category>                  Show all items in selected category
  -s, show <category> <item>           Show description of item

  -a, add                              Add new item

  -f, find <item>                      Find description of selected item

  -e, export all                       Export All items to qiita private
  -e, export <category>                Export items in selected category to qiita private
  '''

    print(string)
