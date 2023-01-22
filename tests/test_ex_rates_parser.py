import unittest  
from xml.sax import make_parser, handler
from xml.sax import parse
from pathlib import Path
import sys
from kursroz.ex_rates_parser import ExRatesParser

THIS_DIR = Path(__file__).parent

class ExRateParserTests(unittest.TestCase):
    def testParsingXML(self):
        data = None
        with open(THIS_DIR / 'TabelaA.xml', encoding='latin-1') as f:
            data = f.read()
        parser = make_parser()
        parser.setFeature(handler.feature_namespaces,True)
        parser.setFeature(handler.feature_validation,False)
        parser.setFeature(handler.feature_external_ges, False)
        print(sys.path)
        items = parse(data, ExRatesParser()) 
