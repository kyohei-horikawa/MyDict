from os.path import expanduser
import subprocess


def reset():
    home = expanduser("~")
    subprocess.run(['rm', f'{home}/dictionary.db'])
