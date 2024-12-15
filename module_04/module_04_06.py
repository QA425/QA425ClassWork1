num = int(input("Введите число для возведения в степень: "))
start = int(input("Введите с какой степени начнем: "))
end = int(input("Введите по какую степень возводить: "))

for exp in range(start, end + 1):
    result = num ** exp
    print(f'{num} в степени {exp}, равно {result}')
print()

for i in range(start, end + 1):
    result = num ** i
    print(f'{num} в степени {i}, равно {result}')
print()