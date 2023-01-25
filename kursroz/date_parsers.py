from datetime import datetime

def parse_date(str):
    #Tue, 20 Dec 2022 11:45:01 +0100,
    return datetime.strptime(str, '%a, %d %b %Y %H:%M:%S %z')

