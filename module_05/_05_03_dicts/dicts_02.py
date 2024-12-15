# pets_dict = {'cat': 'Котейка'}
# pets_dict['dog'] = 'Собачка'
# print(pets_dict)
# print()
#
# pets_dict['cat'] = 'Кошка'
# pets_dict['dog'] = 'Собака'
# print(pets_dict)
# print()
#
# del pets_dict['cat']
# print(pets_dict)


pets_dict = {'cat': 'Кошка', 'dog': 'Собака'}
shop_dict = {'parrot': 'Попугай', 'snake': 'Змея'}

pets_dict.update(shop_dict)
print(pets_dict)

pets_dict = {'cat': 'Кошка', 'dog': 'Собака'}
shop_dict = {'parrot': 'Попугай', 'dog': 'Змея'}

pets_dict.update(shop_dict)
print(pets_dict)
