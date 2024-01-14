import pytest
from src.data.data_manager import File

@pytest.mark.sorted_test
def test_sort_data(temp_json):
    test_file = File(temp_json)
    new_file = test_file.give_sort_file(test_file.open_file, 5)
    print(new_file)
    assert new_file[0]['date'] > new_file[1]['date'] > new_file[2]['date'] > new_file[3]['date'] > new_file[4]['date']