import csv

class CSVHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        with open(self.file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        return data

    def print_page(self, data, page=1, page_size=10):
        start = (page - 1) * page_size
        end = start + page_size
        page_data = data[start:end]
        for item in page_data:
            print(item)
        print(f"\nPage {page}/{(len(data) - 1) // page_size + 1}")
