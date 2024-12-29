data_dict = {"v": 60, "t": 3}


def calculate_vay(v, t):
    way = v * t
    return way


print('Распаковка словаря', calculate_vay(**data_dict))
# print('Распаковка словаря', calculate_vay(v=60, t=30))


