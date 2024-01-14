import pytest
import json

@pytest.mark.test_fixture
def test_fixture_json(temp_json):
    """Тестировка фикстуры которая имеет хранилище тестового JSON
        Получает Фикстуру
        Загружает JSON из фикстуры
        Проверяет корректность
        
    Args:
        temp_json (fixture): Фикстура с хранилищем
    """
    
    with temp_json.open() as f:
        json_file = json.load(f)
        
    assert json_file[0]['operationAmount']['amount'] == "31957.58"

@pytest.mark.test_fixture
def test_fixture_open(file_print):
    """ Тест фисктуры имеющая уже открытый JSON
        Получает фикстуру с списком
        Проверяет корректность по ключу
        
    Args:
        file_print (fixture): Фикструра с Списком из JSON
    """    
    assert file_print[0]['operationAmount']['amount'] == "31957.58"
    
@pytest.mark.test_fixture
@pytest.mark.xfail
def test_fail_fixture(temp_json):
    """ Тест который ожидает fail
        Получает фикстуру с временным файлом
        Открывает JSON
        Проверяет корректность
        
    Args:
        temp_json (fixture): Фикстура с хранилищем
    """    
    with temp_json.open() as f:
        json_file = json.load(f)
        
    assert json_file[0]['id']== 44194584312
    
@pytest.mark.test_fixture 
@pytest.mark.xfail
def test_fail_fixture_open(file_print):
    """Тест который ожидает fail
        Получает фикстуру с списком
        Проверяет корректность по ключу
    Args:
        file_print (fixture): Фикструра с Списком из JSON
    """   
     
    assert file_print[0]['date'] == "2019-08-25T10:50:58.294041"
    
@pytest.mark.test_fixture
def test_fixture_summary(summary_tuple):
    """ Тест фикстуры с инициализированным классом
        Получает фикстуру с классом
        Проверяет корректность кортежем

    Args:
        summary_tuple (fixture): Фикстура с классом
    """   
     
    assert summary_tuple._summary() == (None, None, None, None, None, None)
