import pytest
from src.utils.utils import FileSummary

@pytest.mark.tuple
def test_summary(temp_json):
    """ Тест функции которая создает кортежи

        Получает фикстуру
        Инциализирует класс
        Создает 5 экземпляров кортежа
        Сравнивает корректность кортежей
        
    Args:
        temp_json (fixture): Фикстура содержащая путь к временному файлу
    """ 
      
    file = FileSummary(temp_json)
    file.result = 5
    
    assert file.result[0].time == '26.08.2019'
    assert file.result[0].description == "Перевод организации"
    assert file.result[0].from_ == "Maestro 1596 83** **** 5199 ->"

@pytest.mark.tuple_maker
@pytest.mark.xfail
def test_fail_summary(temp_json):
    """ Тест ожидающий fail

        Получает фикстуру
        Инциализирует класс
        Создает 5 экземпляров кортежа
        Сравнивает корректность кортежей
        
    Args:
        temp_json (fixture): Фикстура содержащая путь к временному файлу
    """    
    
    file = FileSummary(temp_json)
    file.result = 5
    
    assert file.result[3].time == '26.08.2019'

    
@pytest.mark.date
class TestData():
    """ Тестовы класс объединяющий в себе все тесты связанные с параметром 'time'
    """
      
    def test_summary_date1(self, summary_tuple):
        """Тест пустого параметра
            
            Получает фикстуру с классом
            Проверят корректность данных в кортеже
        
        Args:
            summary_tuple (FileSummary): Фикстура с Инциализированным классом
        """        
        assert summary_tuple._summary() == (None, None, None, None, None, None)
        
    def test_summary_date2(self, summary_tuple):
        """ Тест параметра 'time'

            Получает фикстуру с классом
            Проверят корректность данных в кортеже параметра 'time'
            
        Args:
            summary_tuple (FileSummary): Фикстура с Инциализированным классом
        """
                
        assert summary_tuple._summary("2019-07-18T12:27:13.355343") == ("2019-07-18T12:27:13.355343", None, None, None, None, None)
        
    def test_summaty_date_formated(self, summary_tuple):
        """ Тест параметра 'time' с функцией переработки формата
        
            Получает фикстуру с классом
            Проверят корректность данных в кортеже параметра 'time' с функцией переработки формата

        Args:
            summary_tuple (FileSummary): Фикстура с Инциализированным классом
        """  
              
        assert summary_tuple._summary(time=summary_tuple.make_time("2019-07-18T12:27:13.355343")) == ("18.07.2019", None, None, None, None, None)
        
    def test_summary_date_empty(self, summary_tuple):
        """ Тест параметра 'time' с функцией переработки формата с пустым параметром

            Получает фикстуру с классом
            Проверят корректность данных в кортеже параметра 'time' с функцией переработки формата
            
        Args:
            summary_tuple (FileSummary): Фикстура с Инциализированным классом
        """      
          
        assert summary_tuple._summary(time=summary_tuple.make_time()) == (None, None, None, None, None, None)
        
    @pytest.mark.xfail     
    def test_summary_date_duck(self, summary_tuple):
        """ Тест ожидающий fail в проверке функции
        
            Получает фикстуру с классом
            Проверят корректность данных в кортеже параметра 'time' с функцией переработки формата

        Args:
            summary_tuple (FileSummary): Фикстура с Инциализированным классом
        """ 
               
        assert summary_tuple._summary(time=summary_tuple.make_time("2019-07-18T12:27:13.355343")) == ("2019-07-18T12:27:13.355343", None, None, None, None, None)
        
@pytest.mark.card_mask
class TestMask():
    """ Тестовы класс объединяющий в себе все тесты связанные с параметром 'from_'
    """    
    
    def test_summary_card(self, summary_tuple):
        """ Проверка параметра 'from_' в кортеже

            Получает фикстуру с классом
            Проверят корректность данных в кортеже параметра 'from_'
    
        Args:
            summary_tuple (FileSummary): Фикстура с Инциализированным классом
        """ 
               
        assert summary_tuple._summary(from_="Visa Platinum 6942697754917688") == (None, None, "Visa Platinum 6942697754917688", None, None, None)
    
    def test_summary_card_mask(self, summary_tuple):
        """Тест параметра 'from_' с функцией переработки данных

            Получает фикстуру с классом
            Проверят корректность данных в кортеже параметра 'from_' с функцией переработки данных
            
        Args:
            summary_tuple (FileSummary): Фикстура с Инциализированным классом
        """  
              
        assert summary_tuple._summary(from_=summary_tuple.make_mask_visa("Visa Platinum 6942697754917688")) == (None, None, "Visa Platinum 6942 69** **** 7688 ->", None, None, None)
        
    @pytest.mark.parametrize('number, expected_result', [("6942697754917688", "**7688"),
                                                         ("4214241434142144", "**2144"),
                                                         (None, None)])
    def test_mask_account(self, summary_tuple, number, expected_result):
        """ Параметризированный тест с группой проверок номеров без имени
            
            Получает фикстуру и необходимые аргументы
            Сравнивает корректность группы из аргументов
        
        Args:
            summary_tuple (FileSummary): Фикстура с Инциализированным классом
            number (str|None): Номер подающий в функцию
            expected_result (str|None): Ожидаемый номер после переработки его функцией
        """ 
               
        assert summary_tuple.make_mask_account(number) == expected_result
    
    @pytest.mark.parametrize('number, expected_result', [("Visa Platinum 6942697754917688", "Visa Platinum 6942 69** **** 7688 ->"),
                                                         ("Visa 6942697754917688", "Visa 6942 69** **** 7688 ->"),
                                                         ("Счет 6942697754917688", "Счет **7688 ->"),
                                                         (None, "->")])
    def test_summary_mask(self, summary_tuple, number, expected_result):
        """Параметризированный тест с группой проверок номеров с именем или двойным именем
            
            Получает фикстуру и необходимые аргументы
            Сравнивает корректность группы из аргументов

        Args:
            summary_tuple (FileSummary): Фикстура с Инциализированным классом
            number (str|None): Номер подающий в функцию
            expected_result (str|None): Ожидаемый номер после переработки его функцией
        """       
         
        assert summary_tuple.make_mask_visa(number) == expected_result
        
    @pytest.mark.xfail
    @pytest.mark.parametrize('number, expected_result', [("Visa Platinum 6942697754917688", "Visa Platinum 6942697754917688"),
                                                         ("Visa 6942697754917688", "Visa 6942697754917688"),
                                                         ("Счет 6942697754917688", "Счет 6942697754917688"),
                                                         (None, "")])
    def test_summary_mask_duck(self, summary_tuple, number, expected_result):
        """ Ожидающий fail Параметризированный тест с группой проверок номеров с именем или двойным именем
            
            Получает фикстуру и необходимые аргументы
            Сравнивает корректность группы из аргументов

        Args:
            summary_tuple (FileSummary): Фикстура с Инциализированным классом
            number (str|None): Номер подающий в функцию
            expected_result (str|None): Ожидаемый номер после переработки его функцией
        """ 
              
        assert summary_tuple.make_mask_visa(number) == expected_result
        
   
@pytest.mark.formated
@pytest.mark.parametrize("time, expected_result", [("10", "10"),
                                                   ("1", "01"),
                                                   ("9", "09"),
                                                   ("2019", "2019"),
                                                   ("193", "0193")]) 
def test_formated_time(summary_tuple, time, expected_result):
    """ Параметризированный тест с группой проверок чисел на их корректрую переработку для времени

    Args:
        summary_tuple (FileSummary): Фикстура с Инциализированным классом
        time (str): Цифра которая можеть быть 1но, 2ух, 3ох или 4ох значимым
        expected_result (str): Ожидаемый результат после преработки цифры
    """  
      
    assert summary_tuple.get_formated(time) == expected_result
