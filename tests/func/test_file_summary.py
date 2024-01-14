import pytest
from src.utils.utils import FileSummary

@pytest.mark.tuple_maker
def test_summary(temp_json):
    file = FileSummary(temp_json)
    file.result = 5
    assert file.result[0].time == '26.08.2019'
    assert file.result[0].description == "Перевод организации"
    assert file.result[0].from_ == "Maestro 1596 83** **** 5199 ->"

@pytest.mark.tuple_maker
@pytest.mark.xfail
def test_fail_summary(temp_json):
    file = FileSummary(temp_json)
    file.result = 5
    assert file.result[3].time == '26.08.2019'

    
@pytest.mark.summary_date
class TestData():
    def test_summary_date1(self, summary_tuple):
        assert summary_tuple._summary() == (None, None, None, None, None, None)
        
    def test_summary_date2(self, summary_tuple):
        assert summary_tuple._summary("2019-07-18T12:27:13.355343") == ("2019-07-18T12:27:13.355343", None, None, None, None, None)
        
    def test_summaty_date_formated(self, summary_tuple):
        assert summary_tuple._summary(time=summary_tuple.make_time("2019-07-18T12:27:13.355343")) == ("18.07.2019", None, None, None, None, None)
        
    def test_summary_date_empty(self, summary_tuple):
        assert summary_tuple._summary(time=summary_tuple.make_time()) == (None, None, None, None, None, None)
    @pytest.mark.xfail     
    def test_summary_date_duck(self, summary_tuple):
        assert summary_tuple._summary(time=summary_tuple.make_time("2019-07-18T12:27:13.355343")) == ("2019-07-18T12:27:13.355343", None, None, None, None, None)
        
@pytest.mark.summary_mask
class TestMask():
    
    def test_summary_card(self, summary_tuple):
        assert summary_tuple._summary(from_="Visa Platinum 6942697754917688") == (None, None, "Visa Platinum 6942697754917688", None, None, None)
    
    def test_summary_card_mask(self, summary_tuple):
        assert summary_tuple._summary(from_=summary_tuple.make_mask_visa("Visa Platinum 6942697754917688")) == (None, None, "Visa Platinum 6942 69** **** 7688 ->", None, None, None)
        
    @pytest.mark.parametrize('number, expected_result', [("6942697754917688", "**7688"),
                                                         ("4214241434142144", "**2144"),
                                                         (None, None)])
    def test_mask_account(self, summary_tuple, number, expected_result):
        assert summary_tuple.make_mask_account(number) == expected_result
    
    @pytest.mark.parametrize('number, expected_result', [("Visa Platinum 6942697754917688", "Visa Platinum 6942 69** **** 7688 ->"),
                                                         ("Visa 6942697754917688", "Visa 6942 69** **** 7688 ->"),
                                                         ("Счет 6942697754917688", "Счет **7688 ->"),
                                                         (None, "->")])
    def test_summary_mask(self, summary_tuple, number, expected_result):
        assert summary_tuple.make_mask_visa(number) == expected_result
        
    @pytest.mark.xfail
    @pytest.mark.parametrize('number, expected_result', [("Visa Platinum 6942697754917688", "Visa Platinum 6942697754917688"),
                                                         ("Visa 6942697754917688", "Visa 6942697754917688"),
                                                         ("Счет 6942697754917688", "Счет 6942697754917688"),
                                                         (None, "")])
    def test_summary_mask_duck(self, summary_tuple, number, expected_result):
        assert summary_tuple.make_mask_visa(number) == expected_result
        
   
@pytest.mark.formated
@pytest.mark.parametrize("time, expected_result", [("10", "10"),
                                                   ("1", "01"),
                                                   ("9", "09"),
                                                   ("2019", "2019"),
                                                   ("193", "0193")]) 
def test_formated_time(summary_tuple, time, expected_result):
    assert summary_tuple.get_formated(time) == expected_result
