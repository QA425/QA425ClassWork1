# pets_dict = {'cat': 'Кошка', 'dog': 'Собака'}
# print(pets_dict['dict'])

# animal = 'snake'
# if animal in pets_dict:
#     print(pets_dict[animal])
# else:
#     print(f'{animal} нет в словаре!')
#
#
# animal = 'snake'
# try:
#     print(pets_dict[animal])
# except KeyError as KE:
#     print(type(KE).__name__)
#     print(f'{animal} нет в словаре!')
# finally:
#     print(f'Программа завершила свою работу!')

pets_dict = {'cat': 'Кошка', 'dog': 'Собака'}
get_animal = pets_dict.get('cat')
print(get_animal)
get_animal_1 = pets_dict.get('bird')
print(get_animal_1)
print()

set_animal = pets_dict.setdefault('cat')
print(set_animal)
set_animal_1 = pets_dict.setdefault('bird')
print(set_animal_1)
print(pets_dict)

set_animal_2 = pets_dict.setdefault('snake', 'Змея')
print(set_animal_2)
print(pets_dict)
