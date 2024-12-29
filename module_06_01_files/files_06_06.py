"""Можете дополнительно подумать как разбить данный код на отдельные функции (2)"""
def get_shopping_data(filename):
    items_count = 0
    items_sum = 0
    row_index = 0
    try:
        with open(filename, encoding='utf-8') as file:
            for item_data in file:
                row_index += 1
                if item_data.count(' || ') < 2:
                    print(f'!!!В строке {row_index} есть ошибка {item_data.strip()}!!!')
                    continue
                temp_data = item_data.strip().split(' || ')
                item, quantity, price = temp_data
                items_count += 1
                items_sum += float(quantity) * float(price)
    except FileNotFoundError:
        return 'Файл не найден'
    return items_count, items_sum


my_filename = r'files\shopping_list.txt'
my_count, my_sum = get_shopping_data(my_filename)
print(f'В списке {my_count} позиций, общая сумма {my_sum} рублей.')
