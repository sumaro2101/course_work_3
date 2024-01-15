from src.data.data_manager import File
from collections import namedtuple

class FileSummary(File):
    """Основной класс-инструмент работы с файлом

    Args:
        File (class): Наследуется от класса File
    """    
    # Инициализация в классе именованого кортежа
    _summary = namedtuple('Summary', ['time', 'description', 'from_', 'to', 'amount', 'valute'])
    _summary.__new__.__defaults__ = (None, None, None, None, None, None)
    
    @classmethod
    def get_formated(cls, time) -> str:
        """Форматирует время в зависимости количества символов

        Args:
            time (str): Получает время для обработки

        Returns:
            str: Возращает готовый формат
        """ 
            
        if len(time) <= 2:
            return time.rjust(2, '0')
        
        if len(time) <= 4:
            return time.rjust(4, '0')
        
    @classmethod
    def make_time(cls, time=None) -> str:
        """ Вычленяет из строки необходимый для обработки формат времени

        Args:
            time (str, optional): Получает строку из которой нужно выделить время

        Returns:
            str: Возращает необходимый формат для дальнейшей обработки
        """
        
        if time is None:
            return None
        
        result = time.split("T")[0].split("-")
        return ".".join(result[::-1])
        
    @classmethod 
    def make_mask_account(cls, number=None) -> str:
        """ Скрывает часть строки состоящей их цифр для Счетов
        Если в аргумент попал number состоящий из 2 элементов (Счет 432142341)
        Тогда он возращает Оба обработанных элемента
        
        Если аргумент состоит из одного элемента (431243241)
        Возращает - переработанный один аргумент
        
        Если аргумент (None)
        Возращает - None

        Args:
            number (str, optional): Получает строку из цифр для обработки. Defaults to None.

        Returns:
            str: Отдает готовую строку скрытых цифр
        """  
              
        if number is None:
            return None
        
        if len(number.split(" ")) == 1:
            return "".join(["**", number[-4:]])
        
        name, number = number.split(" ")
        number = "".join(["**", number[-4:]])
        return f'{name} {number}'
   
    @classmethod
    def make_mask_visa(cls, card=None, digits_spase=4, mask_char='*') -> str:
        """Получает имя и номер карты и перерабатывает ее
        Если Аргумент card состоит из двух элементов (Visa 42314324423142)
        Отдает (Visa 4122 43** **** 4324 ->)
        
        Если card состоит из трех элементов (Visa Platinum 42343214124)
        Отдает (Visa Platinum 4321 32** **** 3241 ->)
        
        Если None
        Отдает None

        Args:
            card (str, optional): Имя и Номер карты. Defaults to None.
            digits_spase (int, optional): Количество цифр между пробелами. Defaults to 4.
            mask_char (str, optional): Симвод для скрытия номера. Defaults to '*'.

        Returns:
            str: Возращает переработанную строку из имени и скрытого номера
        """        
        
        if card is None:
            return "->"
        
        if len(card.split(" ")) == 2:
            name, number = card.split(' ')
            
            if name == "Счет" or name == "МИР":
                result = cls.make_mask_account(number)
                return f"{name} {result} ->"
            
            number = "".join([number[:6], mask_char * len(number[6:-4]), number[-4:]])
            result = " ".join(map("".join, zip(*[iter(number)] * digits_spase)))
            return f"{name} {result} ->"

        if len(card.split(" ")) == 3:
            name_visa, type_visa, number = card.split(' ')
            number = "".join([number[:6], mask_char * len(number[6:-4]), number[-4:]])
            result = " ".join(map("".join, zip(*[iter(number)] * digits_spase)))
            return f'{name_visa} {type_visa} {result} ->'
    
    @classmethod
    def print_result(cls, item) -> str:
        """Выводит всю информацию в нужном виде

        Args:
            item (tuple): Получает кортеж со всеми переботанными и готовыми данными

        Returns:
            str: Отдает все информацию в готовом виде
        """
              
        return f'''{item.time} {item.description}
{item.from_} {item.to}
{item.amount} {item.valute}\n'''
    
    @property    
    def result(self) -> tuple:
        """Возращает готовый кортеж

        Returns:
            tuple: Возращает кортеж со всем готовыми данными
        """
            
        return self.__result
    
    @result.setter
    def result(self, count_files) -> None:
        """Сбор и объединение всей информации в кортеж

        Args:
            count_files (int): Количество кортежей которое необходимо создать, этот же аргумент переходит в сортировочную функцию
        """        
        self.__result = [self._summary(time=self.make_time(item.get('date')),
                                        description=item.get('description'),
                                        from_=self.make_mask_visa(item.get('from')),
                                        to=self.make_mask_account(item.get('to')),
                                        amount=float(item.get('operationAmount').get('amount', None)),
                                        valute=item.get('operationAmount').get('currency', None).get('name', None))
                         for item in self.give_sort_file(self.open_file, count_files)]
              