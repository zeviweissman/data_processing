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


def test_parse_avg_damage_by_country_dict():
    res = convert_utils.parse_avg_damage_by_country_dict({"Israel": 30})
    assert res == {"country": "Israel", "value": 30}


def test_parse_avg_damage_by_country_dicts():
    res = convert_utils.parse_avg_damage_by_country_dicts([{"Israel": 50}, {"Lebanon": 21}])
    assert res == [{"country": "Israel", "value": 50}, {"country": "Lebanon", "value": 21}]


def test_parse_total_damage_by_attack_type_dict():
    res = convert_utils.parse_total_damage_by_attack_type_dict({"Gun": 20})
    assert res == {"type": "Gun", "value": 20}


def test_parse_total_damage_by_attack_type_dicts():
    res = convert_utils.parse_total_damage_by_attack_type_dicts([{"Gun": 20}, {"Knife":10}])
    assert res == [{"type": "Gun", "value": 20}, {"type": "Knife", "value": 10}]


def test_parse_total_damage_by_group_dict():
    res = convert_utils.parse_total_damage_by_group_dict({"Hamas": 1000})
    assert res == {"group": "Hamas", "value": 1000}


def test_parse_total_damage_by_group_dicts():
    res = convert_utils.parse_total_damage_by_group_dicts([{"Hamas": 1000}, {"ISIS": 500}])
    assert res == [{"group": "Hamas", "value": 1000}, {"group": "ISIS", "value": 500}]
