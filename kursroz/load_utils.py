import requests
from .parse_utils import *

def load_tabel_a():
    NBP_URL = "http://rss.nbp.pl/kursy/TabelaA.xml"
    response = requests.get(NBP_URL)
    xml = response.text
    items = parse_items(xml)
    return items
        
def load_exchange_rate(url): 
    response = requests.get(url)
    xml = response.text
    rate = parse_usd_rate(xml)
    return rate
