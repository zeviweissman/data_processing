from toolz import pipe
from app.db.mongo.connection import get_mongo_client
from app.pandas_.csv_repository import extended_global_terrorism_df
import app.pandas_.stats_service as stats_service
import app.utils.mongo_service_convert_utils as convert_utils
import app.db.mongo.repository.active_groups_by_country_repository as active_groups_by_country_repository
import app.db.mongo.repository.avg_damage_by_country_repository as avg_damage_by_country_repository
import app.db.mongo.repository.total_damage_by_group_repository as total_damage_by_group_repository
import app.db.mongo.repository.total_damage_by_attack_type_repository as total_damage_by_attack_repository
import app.db.mongo.repository.yearly_attack_pct_change_by_country_repository as yearly_attack_pct_change_by_country_repository

raw_data_df = extended_global_terrorism_df


def insert_active_groups_by_country():
    active_groups_by_country = pipe (
        stats_service.active_groups_by_country(raw_data_df),
        convert_utils.series_to_dict,
        convert_utils.parse_active_groups_by_country_dicts
        )
    active_groups_by_country_repository.insert_many(active_groups_by_country)

def insert_avg_damage_by_country():
    avg_damage_by_country = pipe(
        stats_service.avg_damage_by_country(raw_data_df),
    convert_utils.series_to_dict,
        convert_utils.parse_avg_damage_by_country_dicts
    )
    avg_damage_by_country_repository.insert_many(avg_damage_by_country)


def insert_total_damage_by_attack_type():
    total_damage_by_attack_type = pipe(
        stats_service.total_damage_by_attack_type(raw_data_df),
            convert_utils.series_to_dict,
        convert_utils.parse_total_damage_by_attack_type_dicts
            )
    total_damage_by_attack_repository.insert_many(total_damage_by_attack_type)


def insert_total_damage_by_group():
    total_damage_by_group = pipe(
        stats_service.total_damage_by_group(raw_data_df),
    convert_utils.series_to_dict,
        convert_utils.parse_total_damage_by_group_dicts
        )
    total_damage_by_group_repository.insert_many(total_damage_by_group)


def insert_yearly_attack_pct_change_by_country():
    yearly_attacks_pct_change_by_country = pipe(
        stats_service.yearly_attack_pct_change_by_country(raw_data_df),
        convert_utils.series_to_dict,
        convert_utils.parse_yearly_attack_pct_change_by_country_dicts
    )
    yearly_attack_pct_change_by_country_repository.insert_many(yearly_attacks_pct_change_by_country)


def insert_all_stats_to_mongo():
    get_mongo_client().drop_database('terror_attacks')
    insert_active_groups_by_country()
    insert_avg_damage_by_country()
    insert_total_damage_by_attack_type()
    insert_total_damage_by_group()
    insert_yearly_attack_pct_change_by_country()
