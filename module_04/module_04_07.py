# correct_answer = "кот"
# user_answer = input("Домашнее животное пьет молоко говорит мяу: ")
#
# if user_answer == correct_answer:
#     print(f"Верно это {correct_answer}")
# else:
#     print(f"Неверно! Это {correct_answer}")


# str_data = 'привет я строка'
# print(str_data.upper())
#
# str_data_1 = 'ПРИВЕТ Я СТРОКА'
# print(str_data_1.lower())
#
# print(str_data.capitalize())
# print(str_data_1.capitalize())
#
# print(str_data.title())
# print(str_data_1.title())
# print()
#
# str_data_spaces = '  \n\tПРИВЕТ Я СТРОКА  '
# # print(str_data_spaces)
# print(str_data_spaces.strip())
# # print(str_data_spaces.rstrip())
# print(str_data_spaces.lstrip())
#
#
# str_data_spaces = '  \n\tПРИВЕТ Я СТРОКА  '
# print(str_data_spaces.strip().lower())


correct_answer = "кот"
user_answer = input("Домашнее животное пьет молоко говорит мяу: ").strip().lower()

if user_answer == correct_answer:
    print(f"Верно это {correct_answer}")
else:
    print(f"Неверно! Это {correct_answer}")
