from datetime import datetime

def read_str(prompt):
    while True:
        try:
            str = input(prompt)
            return str
        except ValueError:
            print("You've entered a wrong string. Try again...")
            pass

def read_date(prompt, format):
    while True:
        try:
            str = input(prompt)
            date = datetime.strptime(str, format)
            return date
        except ValueError:
            print("You've entered a wrong date. Try again...")
            pass

def read_double(prompt): 
    while True:
        try:
            str = input(prompt)
            value = float(str)
            return str
        except ValueError:
            print("You've entered a wrong value. Try again...")
            pass



