# file = open(r'files\managers_data.txt', 'r', encoding='utf-8')
# content = file.read()
# file.close()
# print(content)
#
# with open(r'files\managers_data.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#
# print(content)

filename = r'files\managers_data.txt'

with open(r'files\managers_data.txt', 'r', encoding='utf-8') as file:
    lines_list = []
    for line in file:
        lines_list.append(line.strip())
        print(line.strip())

print(lines_list)

