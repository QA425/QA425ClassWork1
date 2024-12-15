my_dict = {}
print(my_dict)
# print(type(my_dict))
my_dict_1 = dict()
print(my_dict_1)

my_dict_2 = {'Петр': 201, 'Мария': 201}
print(my_dict_2)

my_dict_4 = {('мтс', 'мтс'): 50, 3: 'тип данных int', 2.5: 'тип данных float', 'list_type': ['Петр', 'Мария']}
print(my_dict_4['list_type'][0])

my_dict_5 = dict(Петр='Имя', Python='Язык программирования')
print(my_dict_5)

my_dict_6 = dict((('list_type', ['Петр', 'Мария']), (2.5, 'тип данных float')))
print(my_dict_6)

explanations = {True: "Да все верно!", False: "Это не верно!"}

print(explanations[3 > 2])
print(explanations[3 < 2])
