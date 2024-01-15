from src.utils.utils import FileSummary
import os

# Переменная содержащая путь к JSON
path_json = os.path.join('src', 'data', 'operations.json')
# Количество необходимых объектов
count_objects = 5

# Инициализация класса с путем
file = FileSummary(path_json)
# Создание объектов
file.result = count_objects
# Цикл для вывода поочередно готовых объектов
for i in file.result:
    print(file.print_result(i))