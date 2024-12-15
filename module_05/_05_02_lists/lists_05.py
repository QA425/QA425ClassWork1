# category_list = ["Drama", "Comedy", "Fantasy"]
# print(category_list)
#
# # print(category[0])
# # print(category[1])
# # print(category[2])
# # print(category[-1])
# category_list[0] = 'Action'
# category_list[1] = 'Tragedy'
# category_list[2] = 'Scy-Fy'
# print(category_list)

category_list = ["Drama", "Zomedy", "fantasy", 'Алфавит']
nums_list = [3, 1, 4, 2, 11, 25]
print(len(category_list), len(nums_list))
print(max(category_list), max(nums_list))
print(min(category_list), min(nums_list))
print(sum(nums_list))
print(''.join(category_list))
print()

sorted_category_list = sorted(category_list)
sorted_nums_list = sorted(nums_list)
print(sorted_category_list)
print(sorted_nums_list)

sorted_category_list_rev = sorted(category_list, reverse=True)
sorted_nums_list_rev = sorted(nums_list, reverse=True)
print(sorted_category_list_rev)
print(sorted_nums_list_rev)

example_list_nums = ['03', '1', '02', '11', '0100']
sorted_example_list_nums = sorted(example_list_nums, reverse=True)
print(sorted_example_list_nums)

