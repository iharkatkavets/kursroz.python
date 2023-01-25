import unittest  
from datetime import datetime
from kursroz.date_utils import day_before 

class DateUtilsTests(unittest.TestCase):
    def test_date_before(self):
        self.assertTrue(datetime(2023, 1, 22).date() == day_before(datetime(2023, 1, 23)).date())
        self.assertTrue(datetime(2022, 12, 31).date() == day_before(datetime(2023, 1, 1)).date())
        self.assertTrue(datetime(2023, 2, 28).date() == day_before(datetime(2023, 3, 1)).date())


