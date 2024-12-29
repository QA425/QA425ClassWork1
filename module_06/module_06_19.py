data_list = [60, 2]
data_tuple = (50, 3)


def calculate_vay(v, t):
    way = v * t
    return way


print('Распаковка списка', calculate_vay(*data_list))
print('Распаковка кортежа', calculate_vay(*data_tuple))
print(*data_list)
print(*data_tuple)
v, t = data_list
print(v, t)
