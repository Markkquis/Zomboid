import unittest
from csv_handler import CSVHandler

class TestCSVHandler(unittest.TestCase):
    def test_read_csv(self):
        csv_handler = CSVHandler('test_items.csv')
        data = csv_handler.read_csv()
        self.assertGreater(len(data), 0)

if __name__ == '__main__':
    unittest.main()
