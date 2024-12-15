# for i in range(10):
#     print(i)
#
# my_str = "Привет!"
# for i in range(len(my_str)):
#     print(my_str[i])


finish = 10

for i in range(finish):
    print(f"Внутри цикла {i}")

print("Вне цикла")
print()

start = 3
end = 7

for i in range(start, end):
    print(f"Внутри цикла {i}")

print("Вне цикла")
print()

for i in range(0, 50, 10):
    print(f"Внутри цикла {i}")

print("Вне цикла")
print()

start = 0
end = 50
step = 10

for i in range(start, end, step):
    print(f"Внутри цикла {i}")

print("Вне цикла")
