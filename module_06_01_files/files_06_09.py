import json
from json import JSONDecodeError


def get_data_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            json_data = file.read()
            python_data = json.loads(json_data)
    except FileNotFoundError:
        return 'Файл не найден!'
    except JSONDecodeError:
        return 'Ошибка декодирования файла'
    return python_data


my_filename = r'files\levels.json'
my_data = get_data_json(my_filename)
print(my_data)
if type(my_data) is dict:
    print(my_data['2'])
