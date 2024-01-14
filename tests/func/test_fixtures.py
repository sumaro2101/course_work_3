import pytest
import json

@pytest.mark.test_fixture
def test_fixture_json(temp_json):
    ''' Тест фикстуры, вывод json файла '''
    
    with temp_json.open() as f:
        json_file = json.load(f)
    assert json_file[0]['operationAmount']['amount'] == "31957.58"

@pytest.mark.test_fixture
def test_fixture_open(file_print):
    assert file_print[0]['operationAmount']['amount'] == "31957.58"
    
@pytest.mark.test_fixture
@pytest.mark.xfail
def test_fail_fixture(temp_json):
    with temp_json.open() as f:
        json_file = json.load(f)
    assert json_file[0]['id']== 44194584312
    
@pytest.mark.test_fixture 
@pytest.mark.xfail
def test_fail_fixture_open(file_print):
    assert file_print[0]['date'] == "2019-08-25T10:50:58.294041"
    
@pytest.mark.test_fixture
def test_fixture_summary(summary_tuple):
    assert summary_tuple._summary() == (None, None, None, None, None, None)
