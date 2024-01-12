import pytest
from src.utils.utils import FileSummary

@pytest.mark.tuple_maker
def test_summary(temp_json):
    file = FileSummary(temp_json)
    file.result = 5
    assert file.result[0].time == '2019-08-26'
    assert file.result[0].description == "Перевод организации"
    assert file.result[0].from_ == "Maestro 1596837868705199"

@pytest.mark.tuple_maker
@pytest.mark.xfail
def test_fail_summary(temp_json):
    file = FileSummary(temp_json)
    file.result = 5
    assert file.result[3].time == '2019-08-423'
    assert file.result[4].description == "Перевод организации"
    assert file.result[2].from_ == "Maestro 1596837868705199"