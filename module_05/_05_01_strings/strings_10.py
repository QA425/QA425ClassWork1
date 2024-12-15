print("15 \\ 2 = 7.5")
print("Имя \"Цитата\"")
print('Имя \'Цитата\'')
print('Имя "Цитата"')
print('It\'s alright')
print("В Python последовательность\nотвечает за перенос строки")
print("В Python последовательность \\n отвечает за перенос строки")

filepath = 'test_dir\\test.txt'

with open(filepath, 'w', encoding='utf-8') as file:
    file.write('Hello world!')
