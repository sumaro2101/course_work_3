import os
import pytest
import json

from src.data import File


def test_data_manager(temp_json):
    ''' Проверка функции открытия файла '''

    # Получает путь к файлу
    # Окрывает файл
    # Сравнивает с фикстурой
    t_test = File(temp_json)
    with temp_json.open() as f:
        expected = json.load(f)
    assert t_test.open_file == expected

def test_empty():
    
    with pytest.raises(TypeError):
        t_test = File()
