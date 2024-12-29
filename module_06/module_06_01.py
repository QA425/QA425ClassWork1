import random


def display_random_gift():
    gifts = ["барбариски", "мячик", "машинка", "конструктор"]
    random_gift = random.sample(gifts, 1)[0]

    print(random_gift)
    return "функция отработала"


while True:
    user_input = input("Введите stop для остановки или enter для выбора случайного подарка")
    if user_input == 'stop':
        break
    display_random_gift()
