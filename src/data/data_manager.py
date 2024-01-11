import json
import os

file_data = os.path.join('src', 'data', 'operations.json')
class File:

    def __init__(self, file=None):
        self._validate(file)
        self.open_file = file

    @classmethod
    def _validate(cls, file):
        """_summary_

        Args:
            file (_type_): _description_

        Raises:
            TypeError: _description_
        """                
        if file is None:
            raise TypeError("Файл не найден")

    @property
    def open_file(self):
        return self.__file
    
    @open_file.setter
    def open_file(self, path_file):
        with open(path_file, encoding="utf-8") as file:
            self.__file = json.load(file)
 