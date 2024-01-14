import json
from operator import itemgetter

class File:
    """
    Главный класс работы с файлами JSON
    """
    
    def __init__(self, file=None):
        """ Инициализация класса, получает путь к файлу

        Args:
            file (_type_, optional): Здесь записывается путь. Дефолт None
        """        
        self._data_validate(file)
        self.open_file = file
        
    @classmethod
    def give_sort_file(cls, list_, count_files) -> list:
        """ Сортировка JSON файла по значению

        Args:
            list_ (_type_): Получение JSON файла для работы
            count_files (_type_): Количество Объектов для вывода

        Returns:
            _type_: Возращатеся type: list с количеством объектов указанным в аргументе
        """
              
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
    def open_file(self) -> list:
        """ Возращает переработанный JSON файл

        Returns:
            list: Список 
        """
             
        return self.__file
    
    @open_file.setter
    def open_file(self, path_file) -> None:
        """ Открывает файл и перерабатывает его

        Args:
            path_file (_type_): Получает путь при инициализации к JSON файлу
        """        
        with open(path_file, encoding="utf-8") as file:
            self.__file = json.load(file)
 