import sys
import add
import show
import init
import help
import find
import export


def handler():
    if len(sys.argv) > 1:
        # myDict init
        if sys.argv[1] == 'init':
            init.initialize()
        # myDict add
        elif sys.argv[1] == 'add' or sys.argv[1] == '-a':
            add.add()

        elif sys.argv[1] == 'show' or sys.argv[1] == '-s':
            # myDict show
            if len(sys.argv) == 2:
                show.showAllCategories()

            elif len(sys.argv) == 3:
                # myDict show all
                if sys.argv[2] == 'all':
                    show.showAll()
                # myDict show <category>
                else:
                    show.showItemsInCategory(sys.argv[2])
            # myDict show <category> <name>
            elif len(sys.argv) == 4:
                show.showItem(sys.argv[2], sys.argv[3])
        # myDicy help
        elif sys.argv[1] == 'help' or sys.argv[1] == '-h':
            help.help()

        # myDict find <item>
        elif sys.argv[1] == 'find' or sys.argv[1] == '-f':
            find.find(sys.argv[2])

        # myDict export
        elif sys.argv[1] == 'export' or sys.argv[1] == '-e':
            if len(sys.argv) == 2:
                # myDict export all
                if sys.argv[2] == 'all':
                    export.exportAll()
                # myDict export <category>
                else:
                    export.exportSelectedItem()


if __name__ == "__main__":
    handler()
