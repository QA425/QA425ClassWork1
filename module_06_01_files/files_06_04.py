# with open(r'files\write_data.txt', 'wt', encoding='utf-8') as file:
#     file.write('Hello\n')
#     file.write('World\n')
#     file.write('NewLine\n')

# with open(r'files\write_data.txt', 'at', encoding='utf-8') as file:
#     file.write('Hello\n')
#     file.write('World\n')
#     file.write('NewLine\n')

def write_user_data(filename, user_data):
    with open(filename, 'w', encoding='utf-8') as file:
        for data in user_data:
            file.write(f'{data}\n')
    return 'Данные успешно записаны!'


user_name = input('Введите ваше имя: ')
user_language = input('Какой язык вы изучаете: ')
user_time = input('Как долго: ')
user_institution = input('Где: ')
my_filename = fr'files\{user_name}_answers.txt'
user_data_list = [user_language, user_time, user_institution]
print(write_user_data(my_filename, user_data_list))
