# virus_code = 'print("Я вирус")'
#
# with open('files_06_05.py', 'a', encoding='utf-8') as file:
#     file.write(f'\n{virus_code}\n')


virus_code = 'print("Я вирус")'

with open('files_06_05.py', 'r', encoding='utf-8') as file:
    content = file.read()
    if virus_code in content:
        print("Вирус обнаружен!")
        clean_content = content.replace(virus_code, '')
        with open('files_06_05.py', 'w', encoding='utf-8') as clean_file:
            clean_file.write(clean_content)
    else:
        print('Вирусов нет!')

