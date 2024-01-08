import unittest
from kursroz.report_generator import ReportBuilder
from kursroz.report_generator import ReportGenerator
from datetime import datetime

class MdReportGeneratorTests(unittest.TestCase):
    def test_generate(self):
        report = ReportBuilder.report()\
        .with_invoice_title("1/1/2023")\
        .with_invoice_value("1000")\
        .with_invoice_date(datetime(2023,1,31))\
        .with_money_receive_date(datetime(2023,2,7))\
        .generate()



    def test_decimal(self):
        pass

        



