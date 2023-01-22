import requests

class ExRatesFetcher:
    def __init__(self, url) -> None:
        self.url = url

    def fetch(self):
        response = requests.get(self.url)
        xml = response.text
        print(xml)
        return xml

