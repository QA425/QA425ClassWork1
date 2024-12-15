
my_item_1 = 'item_1'
my_item_2 = 'item_2'

print(my_item_1, my_item_2)
print(my_item_1, my_item_2, sep=' : ')
print(my_item_1, my_item_2, sep=' : ')
print()
print(my_item_1, end=' * ')
print(my_item_2)


def my_func(a: int, b: int):
    """Функция принимает 2 аргумента и возвращает их сумму"""
    c = a + b
    d = a * b
    return c, d

print(my_func)
