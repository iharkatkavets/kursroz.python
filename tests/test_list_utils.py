import unittest  
from datetime import datetime
from kursroz.list_utils import select_item 
from kursroz.item_metadata import ItemMetadata

class ListUtilsTests(unittest.TestCase):
    def test_sort_items(self):
        item0 = ItemMetadata("Item0",datetime(2023,1,20),"http://item0","http://item0")
        item1 = ItemMetadata("Item3",datetime(2023,1,23),"http://item3","http://item3")
        item2 = ItemMetadata("Item4",datetime(2023,1,24),"http://item4","http://item4")
        item3 = ItemMetadata("Item5",datetime(2023,1,25),"http://item4","http://item4")
        unsorted = [item2, item0, item1, item3]
        self.assertEqual(item3, select_item(unsorted, datetime(2023,1,25)))
        self.assertEqual(item2, select_item(unsorted, datetime(2023,1,24)))
        self.assertEqual(item1, select_item(unsorted, datetime(2023,1,23)))
        self.assertEqual(item0, select_item(unsorted, datetime(2023,1,22)))
        self.assertEqual(item0, select_item(unsorted, datetime(2023,1,21)))
        self.assertEqual(item0, select_item(unsorted, datetime(2023,1,20)))


