from xml.sax import parse
from xml.sax.handler import ContentHandler

class ExRatesParser(ContentHandler):
    def startElement(self, name, attrs):
        print(f"BEGIN: <{name}>, {attrs.keys()}")

    def endElement(self, name):
        print(f"END: </{name}>")

    def characters(self, content):
        if content.strip() != "":
            print("CONTENT:", repr(content))
