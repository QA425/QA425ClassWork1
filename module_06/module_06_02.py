import random


def get_random_gift():
    gifts = ["барбариски", "мячик", "машинка", "конструктор"]
    random_gift = random.sample(gifts, 1)[0]

    return random_gift


while True:
    user_input = input("Введите stop для остановки или enter для выбора случайного подарка")
    if user_input == 'stop':
        break
    our_gift = get_random_gift()
    print(f'Вы выиграли {our_gift}')
