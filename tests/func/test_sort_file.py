import pytest
from src.data.data_manager import File

@pytest.mark.sorted_test
def test_sort_data(temp_json):
    """ Тест сортировки JSON файла, очистки от лишних символов а так же вывод определенного количества объектов

        Получает фикстуру с тестовым файлом
        Инициазирует класс
        Записывает в переменную новый отсортированный файл с указанным количеством объектов
        Сравнивает порядок сортировки
        
    Args:
        temp_json (fixture): фикстура с тестовым файлом
    """  
      
    test_file = File(temp_json)
    new_file = test_file.give_sort_file(test_file.open_file, 5)
    
    assert new_file[0]['date'] > new_file[1]['date'] > new_file[2]['date'] > new_file[3]['date'] > new_file[4]['date']