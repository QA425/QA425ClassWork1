# my_str = 'Hello World!'
#
# string_slice = my_str[0:5]
# print(string_slice)
#
# string_slice1 = my_str[:5]
# print(string_slice1)
#
# string_slice2 = my_str[6:11 + 1]
# print(string_slice2)
#
# string_slice3 = my_str[6:]
# print(string_slice3)
# print()
# print('Срезы по отрицательным индексам')
# string_slice4 = my_str[-6:]
# print(string_slice4)
#
# string_slice5 = my_str[:-7]
# print(string_slice5)
#
# string_slice6 = my_str[-6:-3]
# print(string_slice6)
#
# string_slice7 = my_str[-6:11]
# print(string_slice7)
#
# index_1 = 2
# index_2 = 7
#
# print(my_str[index_1:index_2])

my_str = 'Hello World! Hello Python!'
string_step_slice = my_str[6:20:2]
print(string_step_slice)

my_str = 'Hello World! Hello Python!'
string_step_slice = my_str[3::2]
print(string_step_slice)

my_str = 'Hello World! Hello Python!'
string_step_slice = my_str[:20:2]
print(string_step_slice)

my_str = 'Hello World! Hello Python!'
string_step_slice = my_str[:20:4]
print(string_step_slice)

my_str = 'Hello World! Hello Python!'
string_step_slice = my_str[::-1]
print(string_step_slice)

my_str = 'Hello World! Hello Python!'
string_step_slice = my_str[::-2]
print(string_step_slice)
