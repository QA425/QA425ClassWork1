weather = input("Введите какая сегодня погода: 1 - хорошая/2 - плохая: ")

if weather == "1":
    print("Идем гулять!")
    print("Хорошо проведем время")
else:
    tickets = input("Есть ли билеты: да - 1/нет - 2")
    if tickets == "1":
        print("Идем в кино")
    else:
        table = input("Есть ли столик: да - 1/нет - 2")
        if table == '1':
            print('Идем в ресторан')
        else:
            print('Вечер пиццы и настолок!')
