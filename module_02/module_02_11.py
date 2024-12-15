account = int(input("Сумма которая внесена на счет: "))
account = abs(account)

if account > 0:
    withdrawal = int(input("Введите сумму для снятия: "))
    withdrawal = abs(withdrawal)
    if account > withdrawal:
        account -= withdrawal
        print(f"Вот ваши {withdrawal}")
        print(f"Остаток {account}")
    else:
        print(f"Недостаточно средств! На счете всего {account}")
else:
    print("Денег на счете нет вовсе!")
