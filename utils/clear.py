import os

def screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')