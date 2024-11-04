import sys
from csv_handler import CSVHandler
from data_manager import DataManager

def main():
    file_path = 'items.csv'  # Задайте шлях до вашого CSV-файлу
    csv_handler = CSVHandler(file_path)
    data = csv_handler.read_csv()
    data_manager = DataManager(data)

    while True:
        print("\n1. Вивести предмети (посторінково)")
        print("2. Отримати предмет по ID")
        print("3. Пошук предмета по назві")
        print("4. Отримати процентне відношення по стану")
        print("5. Вихід")
        choice = input("Виберіть опцію: ")

        if choice == '1':
            page = int(input("Введіть номер сторінки: "))
            csv_handler.print_page(data, page)
        elif choice == '2':
            item_id = input("Введіть ID предмета: ")
            item = data_manager.get_item_by_id(item_id)
            print(item if item else "Предмет не знайдено.")
        elif choice == '3':
            name = input("Введіть назву для пошуку: ")
            results = data_manager.search_by_name(name)
            for result in results:
                print(result)
        elif choice == '4':
            percentages = data_manager.condition_percentages()
            for condition, percent in percentages.items():
                print(f"{condition}: {percent:.2f}%")
        elif choice == '5':
            sys.exit()
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
