import random

# cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
# print(cinema_category_list)
# random.shuffle(cinema_category_list)
# print(cinema_category_list)
# print()
#
# cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
# # genres_sample = random.sample(cinema_category_list, len(cinema_category_list))
# genres_sample = random.sample(cinema_category_list, 2)
# print(genres_sample)
# print()
#
# some_str = "Привет! Я Строка!"
# items = random.sample(some_str, len(some_str))
# print(items)
# result_str = ''.join(items)
# print(result_str)
# print()


cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
# random_category = random.choice(cinema_category_list)
# print(random_category)

for i in range(len(cinema_category_list)):
    random_category = random.choice(cinema_category_list)
    cinema_category_list.remove(random_category)
    print(random_category)


