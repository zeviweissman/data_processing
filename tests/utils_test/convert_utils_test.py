from pandas import Series

import app.utils.convert_utils as convert_utils



def test_dict_to_list_of_dicts():
    res = convert_utils.dict_to_list_of_dicts({"a": 1, "b": 2, "c": 3})
    assert res == [{"a": 1}, {"b": 2}, {"c": 3}]


def test_series_to_dict():
    series = Series(["a", "b", "c"])
    res = convert_utils.series_to_dict(series)
    assert res == [{0: "a"}, {1: "b"}, {2: "c"}]


def test_parse_yearly_attack_pct_change_by_country_dict():
    res = convert_utils.parse_yearly_attack_pct_change_by_country_dict({("Israel", 2000):30})
    assert res == {"country": "Israel", "year": 2000, "value": 30}


def test_parse_yearly_attack_pct_change_by_country_dicts():
    res = convert_utils.parse_yearly_attack_pct_change_by_country_dicts([{("Israel", 2000):30}, {("Israel", 1999): 20}])
    assert res == [{"country": "Israel", "year": 2000, "value": 30}, {"country": "Israel", "year": 1999, "value": 20}]

def test_parse_active_groups_by_country_dict():
    res = convert_utils.parse_active_groups_by_country_dict({("Israel", "Terror group"):10})
    assert res == {"country": "Israel", "value": 10, "group": "Terror group"}

def test_parse_active_groups_by_country_dicts():
    res = convert_utils.parse_active_groups_by_country_dicts([{("Israel", "Terror group"):10}, {("Israel", "Hamas"):100}])
    assert res == [{"country": "Israel", "value": 10, "group": "Terror group"}, {"country": "Israel", "value": 100, "group": "Hamas"}]