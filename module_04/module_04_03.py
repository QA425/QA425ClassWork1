# user_total = 0
# user_expense = input("Введите сумму расходов за месяц: ")
#
#
# while user_expense != 'stop':
#     user_expense_int = int(user_expense)
#     user_total += user_expense_int
#     user_expense = input("Введите сумму расходов за месяц или stop: ")
#
# print(f"Сумма расходов за месяц {user_total}")

shopping_list = []

while True:
    user_goods = input("Введите что вы купили: ")
    if user_goods == 'стоп':
        break
    else:
        shopping_list.append(user_goods)
print(shopping_list)
# [print(element) for element in shopping_list]
for element in shopping_list:
    print(element)

