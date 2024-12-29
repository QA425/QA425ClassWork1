import json


def write_data_to_json(filename, data):
    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json_data)
    return 'Данные записаны успешно!'


my_filename = r'files\levels.json'
levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: True,
    4: False,
    5: None
}

print(write_data_to_json(my_filename, levels))
