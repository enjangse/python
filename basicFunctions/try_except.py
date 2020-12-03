#!/usr/bin/env python3

#import colorssys
import os

os.system("")

# Group of Different functions for different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print('How many cats do you have?')
numCats =  input()
try:
    if int(numCats) >= 4:
        print('Thats a lot cats')
    else:
        print('Thats is less')
except ValueError:
    print(style.RED + 'You did not enter number')
