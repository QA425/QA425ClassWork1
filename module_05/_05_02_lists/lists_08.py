cinema_category_list = ["Drama", "Comedy", "Fantasy", "Drama", "Scy-Fy", "Action"]

for i in range(len(cinema_category_list)):
    if cinema_category_list[i] == "Drama":
        print(i)


item_index = 0
for category in cinema_category_list:
    if category == "Drama":
        print(item_index)
    item_index += 1
