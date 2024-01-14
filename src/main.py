
from src.utils.utils import FileSummary
import os

path_json = os.path.join('src', 'data', 'operations.json')
count_files = 5

file = FileSummary(path_json)
file.result = count_files
for i in file.result:
    print(file.print_result(i))