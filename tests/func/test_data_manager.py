import os
import pytest
import json

from src.data import File

@pytest.mark.class_test
def test_data_manager(temp_json):
    """ Тест открытия файла функцией
    
        Получает фикстуру с путем
        Инициалиализация класса
        Откытие тестового JSON вторым потоком
        Сравнение JSON их двух потоков

    Args:
        temp_json (fixture): Фикстура с временным хранилищем тестового JSON
    """    

    t_test = File(temp_json)
    
    with temp_json.open() as f:
        expected = json.load(f)
        
    assert t_test.open_file == expected

@pytest.mark.class_test
def test_empty():
    """ Тест вывода искючения в случае инициализации без пути к файлу
    """
       
    with pytest.raises(TypeError):
        t_test = File()
