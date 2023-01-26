from datetime import datetime
from .print_utils import *

def read_str(prompt):
    while True:
        try:
            str = input(f"{bcolors.BOLD}{prompt}{bcolors.ENDC}")
            return str
        except ValueError:
            print(f"{bcolors.FAIL}You've entered a wrong string. Try again...{bcolors.ENDC}")
            pass

def read_date(prompt, format):
    while True:
        try:
            str = input(f"{bcolors.BOLD}{prompt}{bcolors.ENDC}")
            date = datetime.strptime(str, format)
            return date
        except ValueError:
            print(f"{bcolors.FAIL}You've entered a wrong date. Try again...{bcolors.ENDC}")
            pass

def read_double(prompt): 
    while True:
        try:
            str = input(f"{bcolors.BOLD}{prompt}{bcolors.ENDC}")
            value = float(str)
            return str
        except ValueError:
            print(f"{bcolors.FAIL}You've entered a wrong value. Try again...{bcolors.ENDC}")
            pass



