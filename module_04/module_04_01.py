even_numbers = 0
odd_numbers = 0

user_number = int(input("Введите число или напишите 0 чтобы остановить программу: "))

while user_number != 0:
    if user_number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
    user_number = int(input("Введите число или напишите 0 чтобы остановить программу: "))

print(f"Количество четных чисел {even_numbers}")
print(f"Количество нечетных чисел {odd_numbers}")


while True:
    user_choice = input("Введите 1 для продолжения цикла 2 для остановки цикла")
    if user_choice == '1':
        print("Цикл продолжается")
    elif user_choice == '2':
        print("Цикл остановлен!")
    else:
        print("Неверный ввод")


user_input = input("Введите 1 для старта программы по алгоритму 1, 2 для старта программы по алгоритму 2")

# while user_input != '1' and user_input != '2':
while user_input not in ['1', '2']:
    print("Ошибка ввода!")
    user_input = input("Введите 1 для старта программы по алгоритму 1, 2 для старта программы по алгоритму 2")

if user_input == '1':
    print("Выполняю программу 1")
elif user_input == '2':
    print("Выполняю программу 2")
