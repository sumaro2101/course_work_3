import pytest

@pytest.mark.print_result
def test_print_result(summary_tuple):
    item = summary_tuple._summary(summary_tuple.make_time("2019-07-18T12:27:13.355343"),
                                  'fasfaf',
                                  summary_tuple.make_mask_visa('visa 8847384717023026'),
                                  summary_tuple.make_mask_account('Счет 43214132421'),
                                  '42314,22',
                                  'USA')
    assert summary_tuple.print_result(item) == f'''18.07.2019 fasfaf
visa 8847 38** **** 3026 -> Счет **2421
42314,22 USA
'''

@pytest.mark.print_result
def test_print_result1(summary_tuple):
    item = summary_tuple._summary(summary_tuple.make_time("2019-07-18T12:27:13.355343"),
                                  'fasfaf', 
                                  summary_tuple.make_mask_visa(None),
                                  summary_tuple.make_mask_account('Счет 8847384717023026'),
                                  '42314,22',
                                  'USA')
    assert summary_tuple.print_result(item) == f'''18.07.2019 fasfaf
-> Счет **3026
42314,22 USA
'''