# cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
# literature_category_list = ["Поэма", "Роман", "Новелла", "Пьеса", "Проза"]
from traceback import print_tb

#
# for item in cinema_category_list:
#     print(item)
# print()
#
#
# if len(cinema_category_list) == len(literature_category_list):
#     for index in range(len(cinema_category_list)):
#         print(cinema_category_list[index])
#         print(literature_category_list[index])

# cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
# cinema_category_list.append('Horror')
# print(cinema_category_list)
# cinema_category_to_extend = ['Detective', 'Mystery']
# cinema_category_list.extend(cinema_category_to_extend)
# print(cinema_category_list)
# cinema_category_list.insert(2, 'Romance')
# print(cinema_category_list)
# print()
#
# if 'Action' in cinema_category_list:
#     cinema_category_list.remove("Action")
# else:
#     print("Жанра нет в списке")
# print(cinema_category_list)
#
# popped_genre = cinema_category_list.pop(2)
# print(popped_genre)
# print(cinema_category_list)

# cinema_category_list.clear()
# print(cinema_category_list)


cinema_category_list = ["Action", "Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
item_index = cinema_category_list.index("Scy-Fy")
print(item_index)

print(cinema_category_list.count('Comedy'))

cinema_category_list.sort()
print(cinema_category_list)
cinema_category_list.sort(reverse=True)
print(cinema_category_list)

cinema_category_list = ["Action", "Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
cinema_category_list.reverse()
print(cinema_category_list)

print("Action" in cinema_category_list)
print("Horror" in cinema_category_list)
print("Action" not in cinema_category_list)
print("Horror" not in cinema_category_list)