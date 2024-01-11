
import json

def test_fixture_json(temp_json):
    ''' Тест фикстуры, вывод json файла '''
    
    with temp_json.open() as f:
        json_file = json.load(f)
    assert json_file[0]['operationAmount']['amount'] == "31957.58"