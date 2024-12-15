# my_str = 'Hello world! Hello python!'
# print(my_str.startswith('H'))
# print(my_str.startswith('Hello'))
# print(my_str.endswith('!'))
# print(my_str.endswith('python!'))
# print()
#
# print(my_str.startswith('world', 6))
# print(my_str.startswith('world', 6, 11))
#
# print(my_str.endswith('Hello', 13, 18))
# print(my_str.endswith('world', 6, 11))

my_str = 'Hello world! Hello python!'
# replaced_string = my_str.replace('Hello', 'Good-bye').replace('world', 'Earth')
replaced_string = my_str.replace('Hello', 'Good-bye')
replaced_string = replaced_string.replace('world', 'Earth')
print(replaced_string)
