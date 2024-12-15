# import math
#
# print(math.factorial(5))

# num_1 = int(input("Введите начало диапазона: "))
# num_2 = int(input("Введите конец диапазона: "))
#
# if num_1 > num_2:
#     num_2, num_1 = num_1, num_2
#
# print(num_1)
# print(num_2)

stars_line = int(input("Введите длину линии"))
line = ''

for i in range(stars_line):
    line += '*'

print(line)


symbols_line = int(input("Введите длину линии"))
symbol = input('Введите желаемый символ')
line = ''

for i in range(symbols_line):
    line += symbol

print(line)
