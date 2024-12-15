# my_str = 'Hello World! Hello Python!'
# element_index = my_str.find('o')
# print(element_index)
# element_index_1 = my_str.find('o', 5)
# print(element_index_1)
# element_index_2 = my_str.find('o', 8, 20)
# print(element_index_2)
# print()

# my_str = 'Hello World! Hello Python!'
# element_index = my_str.index('o')
# print(element_index)
#
# my_str = 'Hello World! Hello Python!'
# my_element = input("Введите элемент для поиска: ")
# if my_element in my_str:
#     print(my_str.index(my_element))
# else:
#     print("Не найдено!!!")
# print()

# my_str = 'Hello World! Hello Python!'
# print(my_str.rfind('o'))
# print(my_str.rfind('o', 0, 22))
# print(my_str.rindex('o'))
# print(my_str.rindex('Z'))

# my_str = 'Hello World! Hello Python!'
# index = 0
#
# for element in my_str:
#     if element == 'o':
#         print(index)
#     index += 1
#
# my_str = 'Hello World! Hello Python!'
# my_str_1 = 'Hello QA425! Hello Python!'
# str_1_indexes_list = []
# str_2_indexes_list = []
#
# for i in range(len(my_str) - 1):
#     if my_str[i] == 'o':
#         str_1_indexes_list.append(str(i))
#     if my_str_1[i] == 'o':
#         str_2_indexes_list.append(str(i))
#
# print(f"Индексы 1й строки: {', '.join(str_1_indexes_list)}")
# print(f"Индексы 2й строки: {', '.join(str_2_indexes_list)}")

# my_str = 'Hello World! Hello Python!'
#
# print(my_str.find('World'))
# print(my_str.index('World'))
# print(my_str.rfind('Hello', 0, 10))
# print(my_str.rindex('Hello'))

my_str = 'Hello World! Hello Python!'
num_of_o_elements = my_str.count('o')
print(num_of_o_elements)

num_of_Hello_elements = my_str.count('Hello')
print(num_of_Hello_elements)
