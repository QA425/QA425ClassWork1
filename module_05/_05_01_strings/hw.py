user_num1 = int(input())
user_num2 = int(input())
user_num3 = int(input())


for i in range(21):
    if user_num1 == i:
        continue
    elif user_num2 == i:
        continue
    elif user_num3 == i:
        continue
    else:
        print(i)

print()
for i in range(21):
    if user_num1 == i or user_num2 == i or user_num3 == i:
        continue
    else:
        print(i)

print()
for i in range(21):
    if i in [user_num1, user_num2, user_num3]:
        continue
    print(i)

# user_nums = input("Введите числа через пробел: ")
# user_nums_list = user_nums.split()
# print(user_nums_list)
# user_nums_list_int = []
#
# for num in user_nums_list:
#     user_nums_list_int.append(int(num))
# print(user_nums_list_int)
