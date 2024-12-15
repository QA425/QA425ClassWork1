# pets_dict = {'Cat': 'Кошка', 'Dog': 'Собака', 'Bird': 'Птица'}
# pets_dict_keys = pets_dict.keys()
# print(pets_dict_keys)
# print(type(pets_dict_keys))
# print(list(pets_dict_keys)[0])
# print()
#
# pets_dict_values = pets_dict.values()
# print(pets_dict_values)
# print(type(pets_dict_values))
# print(list(pets_dict_values)[0])
# print()
#
# pets_dict_items = pets_dict.items()
# print(pets_dict_items)
# print(type(pets_dict_items))
# print(tuple(pets_dict_items))
# items_tuple = tuple(pets_dict_items)
# print(dict(items_tuple))

pets_dict = {'Cat': 'Кошка', 'Dog': 'Собака', 'Bird': 'Птица'}
for key in pets_dict.keys():
    print(key)
print()

for value in pets_dict.values():
    print(value)
print()

for key, value in pets_dict.items():
    print(f'Ключ: {key}. Значение {value}.')
print()

pets_dict_1 = {}
for key, value in pets_dict.items():
    if value == 'Птица':
        continue
    pets_dict_1[key] = value

print(pets_dict_1)

keys_list = []
values_list = []
for key, value in pets_dict.items():
    keys_list.append(key)
    values_list.append(value)
print(keys_list)
print(values_list)
