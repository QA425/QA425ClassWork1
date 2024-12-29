def find_happy_number(number):
    if len(number) != 6:
        return False
    elif not number.isdigit():
        return False
    else:
        num1 = int(number[0]) + int(number[1]) + int(number[2])
        print(num1)
        num2 = int(number[3]) + int(number[4]) + int(number[5])
        print(num2)
        if num1 == num2:
            return True
        else:
            return False


my_number = input("Введите шестизначное число: ")
print(find_happy_number(my_number))
