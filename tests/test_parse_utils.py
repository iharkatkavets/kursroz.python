import unittest  
from pathlib import Path
from kursroz.parse_utils import parse_items, parse_usd_rate

THIS_DIR = Path(__file__).parent

class ParseUtilsTests(unittest.TestCase):
    def testParsingTabelA(self):
        with open(THIS_DIR / 'TabelaA.xml', 'rb') as f:
            items = parse_items(f.read())
            self.assertEqual(25, len(items))

    def testParseUsdRate(self):
        with open(THIS_DIR / 'rates.xml', 'rb') as f:
            rate = parse_usd_rate(f.read())
            self.assertEqual('4,4100', rate)
