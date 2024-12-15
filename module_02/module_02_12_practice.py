# num_1 = int(input("Введите число для проверки: "))
#
#
# if num_1 == 0:
#     print("Это 0")
# elif num_1 % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# num = int(input("Введите текущее число: "))
# num_2 = int(input("Введите второе число: "))
# num_3 = int(input("Введите третье число: "))
#
# if num_2 > num:
#     num = num_2
#
# if num_3 > num:
#     num = num_3
#
# print(f"Наибольшее число = {num}")


# def my_max(nums_list):
#     num_max = 0
#
#     for num in nums_list:
#         if type(num) is int:
#             if num > num_max:
#                 num_max = num
#         else:
#             print("Был замечен неверный тип данных")
#     return num_max
#
#
# my_nums_list = [1, 2, 7, 6, 'sad', 5, 4, 3]
# print(my_max(my_nums_list))

user_rating = input("Введите оценку поездки: ").strip()
print(user_rating)
print(len(user_rating))

if len(user_rating) == 1:
    print("Ужасно!")
elif len(user_rating) == 2:
    print("Очень плохо!")
elif len(user_rating) == 3:
    print("Средненько")
elif len(user_rating) == 4:
    print("Все в порядке")
elif len(user_rating) == 5:
    print("Отлично!")
else:
    print("Ошибка ввода!")
