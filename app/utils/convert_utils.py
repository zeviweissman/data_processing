from typing import List
from toolz import pipe
from pandas import Series


def dict_to_list_of_dicts(dict_to_convert: dict) -> List[dict]:
    return [{key:value} for key, value in dict_to_convert.items()]


def series_to_dict(series: Series) -> List[dict]:
    return pipe(
        series.to_dict(),
        dict_to_list_of_dicts
    )


def parse_yearly_attack_pct_change_by_country_dict(yearly_attack_dict: dict) -> dict:
    return {"country": list(yearly_attack_dict.keys())[0][0], "year": list(yearly_attack_dict.keys())[0][1], "value": list(yearly_attack_dict.values())[0]}


def parse_yearly_attack_pct_change_by_country_dicts(yearly_attacks_dicts: List[dict]) -> List[dict]:
    return [parse_yearly_attack_pct_change_by_country_dict(yearly_attack_dict) for yearly_attack_dict in yearly_attacks_dicts]


def parse_active_groups_by_country_dict(active_groups_dict: dict) -> dict:
    return {"country": list(active_groups_dict.keys())[0][0], "group":list(active_groups_dict.keys())[0][1], "value": list(active_groups_dict.values())[0]}


def parse_active_groups_by_country_dicts(active_groups_dicts: List[dict]) -> List[dict]:
    return [parse_active_groups_by_country_dict(active_group_dict) for active_group_dict in active_groups_dicts]


def parse_avg_damage_by_country_dict(avg_damage_dict: dict) -> dict:
    return {"country": list(avg_damage_dict.keys())[0], "value": list(avg_damage_dict.values())[0]}


def parse_avg_damage_by_country_dicts(avg_damages_dicts: List[dict]) -> List[dict]:
    return [parse_avg_damage_by_country_dict(avg_damages_dict) for avg_damages_dict in avg_damages_dicts]


def parse_total_damage_by_attack_type_dict(total_damage_dict: dict) -> dict:
    return {"type": list(total_damage_dict.keys())[0], "value": list(total_damage_dict.values())[0]}


def parse_total_damage_by_attack_type_dicts(total_damages_dicts: List[dict]) -> List[dict]:
    return [parse_total_damage_by_attack_type_dict(total_damages_dict) for total_damages_dict in total_damages_dicts]


def parse_total_damage_by_group_dict(total_damages_dict: dict) -> dict:
    return {"group": list(total_damages_dict.keys())[0], "value": list(total_damages_dict.values())[0]}


def parse_total_damage_by_group_dicts(total_damages_dicts: List[dict]) -> List[dict]:
    return [parse_total_damage_by_group_dict(total_damages_dict) for total_damages_dict in total_damages_dicts]
