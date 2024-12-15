# cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
# new_cinema_category_list = cinema_category_list
# print(cinema_category_list)
# print(new_cinema_category_list)
# new_cinema_category_list.append('Horror')
# print(new_cinema_category_list)
# print(cinema_category_list)
# print(new_cinema_category_list is cinema_category_list)

cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
new_cinema_category_list = cinema_category_list.copy()
print(new_cinema_category_list is cinema_category_list)
new_cinema_category_list.append('Horror')
print(cinema_category_list)
print(new_cinema_category_list)
print()

new_cinema_category_list_1 = list(cinema_category_list)
new_cinema_category_list_1.append('Horror')
print(cinema_category_list)
print(new_cinema_category_list_1)
print()

new_cinema_category_list_2 = cinema_category_list[:]
new_cinema_category_list_2.append('Horror')
print(cinema_category_list)
print(new_cinema_category_list_2)
print()
