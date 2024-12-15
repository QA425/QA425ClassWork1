prices = {"HDD_Toshiba": 2000, "SSD_Samsung": 8000, "CPU_AMD_Rysen_7": 20000, "CPU_AMD_Rysen_5": 13000, }
user_choice = {}
for i in range(3):
    user_product = input("Что Вы хотите приобрести? ")
    product_quantity = int(input("В каком количестве (в шт): "))

    if user_product in prices:
        total_price = prices[user_product] * product_quantity
        user_choice[user_product] = [product_quantity, total_price]
        print(f"Стоимость {product_quantity} шт {user_product} составляет {total_price} рублей.")
    else:
        print("Извините, у нас нет информации о цене этого товара!")
print()

total = 0
for key, value in user_choice.items():
    print(f'{key} в количестве: {value[0]} штук, общая стоимость {value[1]}')
    total += value[1]
print(f'Общая стоимость {total}')
