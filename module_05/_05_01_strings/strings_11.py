my_path = 'D:\\work_Top_Academy_web\\QA425ClassWork\\module_05\\_05_01_strings'
my_path_raw = r'D:\work_Top_Academy_web\QA425ClassWork\module_05\_05_01_strings'

normal_string = "В Python последовательность\nотвечает за перенос строки"
print(normal_string)

raw_string = r"В Python последовательность \n отвечает за перенос строки (это уже сырая строка)"
print(raw_string)

some_data_list = [r'\n', r'\t', r'\r']
formatted_raw_string = fr"В Python последовательности: {', '.join(some_data_list)} отвечают за работу со строкой (это уже сырая строка)"
print(formatted_raw_string)
