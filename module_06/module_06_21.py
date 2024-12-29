data_list = [60, 2]
data_dict = {"v_d": 60, "t_d": 3}


def calculate_vay(v_l, t_l, v_d, t_d):
    way_l = v_l * t_l
    way_d = v_d * t_d
    return way_l, way_d


my_way_l, my_way_d = calculate_vay(*data_list, **data_dict)
print(f"Распаковка списка/словаря {calculate_vay(*data_list, **data_dict)}")
print(f"Распаковка списка/словаря {my_way_l}, {my_way_d}")
