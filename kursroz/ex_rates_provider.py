from xml.sax import parse
from ex_rates_fetcher import *
from ex_rates_provider import *

NBP_URL = "http://rss.nbp.pl/kursy/TabelaA.xml"

class ExRatesProvider:
    def load(self):
        xml = ExRatesFetcher(NBP_URL).fetch()
        items = parse(xml, ExRatesParser()) 
        print(items)

        
