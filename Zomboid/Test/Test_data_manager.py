import unittest
from data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.items = [
            {'ID': '1', 'Name': 'Hummer', 'Type': 'Tool', 'Condition': 'Mint', 'Amount': '10'},
            {'ID': '2', 'Name': 'Nails', 'Type': 'Fasteners', 'Condition': 'Good', 'Amount': '450'}
        ]
        self.data_manager = DataManager(self.items)

    def test_get_item_by_id(self):
        item = self.data_manager.get_item_by_id('1')
        self.assertIsNotNone(item)
        self.assertEqual(item['Name'], 'Hummer')

    def test_search_by_name(self):
        results = self.data_manager.search_by_name('Nails')
        self.assertEqual(len(results), 1)

    def test_condition_percentages(self):
        percentages = self.data_manager.condition_percentages()
        self.assertIn('Mint', percentages)
        self.assertIn('Good', percentages)

if __name__ == '__main__':
    unittest.main()
