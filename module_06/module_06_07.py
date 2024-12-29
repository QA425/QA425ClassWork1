def calc_sum(numbers):
    _sum = 0
    for number in numbers:
        _sum += int(number)


    return _sum


def main():
    user_numbers = input("Введите числа через пробел: ").split()
    result = calc_sum(user_numbers)
    print(result)


if __name__ == '__main__':
    main()
