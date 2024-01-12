import json


class File:

    
    def __init__(self, file=None):
        self._data_validate(file)
        self.open_file = file
        
    
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
 