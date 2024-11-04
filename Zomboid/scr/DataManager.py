class DataManager:
    def __init__(self, items):
        self.items = items

    def get_item_by_id(self, item_id):
        for item in self.items:
            if item['ID'] == str(item_id):
                return item
        return None

    def search_by_name(self, name):
        results = [item for item in self.items if name.lower() in item['Name'].lower()]
        return results

    def condition_percentages(self):
        condition_count = {}
        total_items = len(self.items)

        for item in self.items:
            condition = item['Condition']
            condition_count[condition] = condition_count.get(condition, 0) + 1

        percentages = {cond: (count / total_items) * 100 for cond, count in condition_count.items()}
        return percentages
