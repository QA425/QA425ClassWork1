def get_managers_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data_list = []
            for manager_data in file:
                data = manager_data.rstrip().split(':')
                data_list.append(data)
    except FileNotFoundError:
        return 'Файл не найден'
    return data_list


managers_data_file = r'files\own_data.txt'
managers_data = get_managers_data(managers_data_file)

for manager, company, head_company in managers_data:
    print(f'{manager} работает в компании {company}, которая принадлежит {head_company}')








