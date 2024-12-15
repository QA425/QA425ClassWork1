pets_dict = {'cat': 'Кошка', 'dog': 'Собака'}
print(pets_dict['cat'])

pets_dict['die Katze'] = pets_dict['cat']
print(pets_dict)
del pets_dict['cat']
print(pets_dict)

# popped_data = pets_dict.pop('dog')
# print(popped_data)
pets_dict['der Hund'] = pets_dict.pop('dog')
print(pets_dict)
