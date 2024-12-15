import random

cinema_category_list = ["Drama", "Comedy", "Fantasy", "Scy-Fy", "Action"]
random_index = random.randint(0, len(cinema_category_list) - 1)
random_category = cinema_category_list[random_index]
print(f'Ваш случайный жанр {random_category}\n')

random.shuffle(cinema_category_list)
random_category = cinema_category_list[0]
print(f'Ваш случайный жанр {random_category}\n')

random_category_list = random.sample(cinema_category_list, 3)
print(f'Ваш случайные жанры {', '.join(random_category_list)}\n')

random_category = random.choice(cinema_category_list)
print(f'Ваш случайный жанр {random_category}\n')


