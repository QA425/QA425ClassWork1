import os

# path_learning = r'D:\work_Top_Academy_web\QA425ClassWork\module_06_01_files'

# for path, dirnames, filenames in os.walk(path_learning):
#     print(f'Путь - {path}')
#     print(f'Директории - {dirnames}')
#     print(f'Файлы - {filenames}')


path_learning = r'D:/work_Top_Academy_web/QA425ClassWork/module_06_01_files'
normalized_path = os.path.normpath(path_learning)
print(normalized_path)

print(os.path.abspath(r'files'))

disk = 'd:\\'
dir_1 = 'work_Top_Academy_web'
dir_2 = 'QA425ClassWork'
dir_3 = 'module_06_01_files'
joined_path = os.path.join(disk, dir_1, dir_2, dir_3)
print(joined_path)

for path, dirnames, filenames in os.walk(joined_path):
    print(f'Путь - {path}')
    print(f'Директории - {dirnames}')
    print(f'Файлы - {filenames}')