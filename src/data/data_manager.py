import json
from operator import itemgetter

class File:
 
    def __init__(self, file=None):
        self._data_validate(file)
        self.open_file = file
        
    @classmethod
    def give_sort_file(cls, list_, count_files):
        return sorted([elem for elem in
                       [item for item in list_ if item]
                       if elem['state'] != 'CANCELED'],
                      key=itemgetter("date"),
                      reverse=True)[:count_files]
    
    @classmethod
    def _data_validate(cls, file):
        """Валидация полученного файла

        Raises:
            TypeError: Если None отдает исключение
        """        
                
        if file is None:
            raise TypeError("Ожидался путь, путь не найден")

    @property
    def open_file(self):
        return self.__file
    
    @open_file.setter
    def open_file(self, path_file):
        with open(path_file, encoding="utf-8") as file:
            self.__file = json.load(file)
 