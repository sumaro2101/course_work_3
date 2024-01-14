
from src.utils.utils import FileSummary
import os

path_json = os.path.join('src', 'data', 'operations.json')

file = FileSummary(path_json)
# print(file.open_file)
file.result = 5
for i in file.result:
    print(i)