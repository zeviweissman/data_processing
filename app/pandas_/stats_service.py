from pandas import DataFrame, Series
from toolz import pipe



def total_damage_by_attack_type(df: DataFrame) -> Series:
    return df.where(df["deadly_score"] >= 0).groupby(["attack_type"])["deadly_score"].sum()


def avg_damage_by_country(df: DataFrame) -> Series:
    return df.where(df['deadly_score'] >= 0).groupby(["country"])["deadly_score"].mean()


def total_damage_by_group(df: DataFrame) -> Series:
    return df.where(df["deadly_score"] >= 0).groupby(["group_name"])["deadly_score"].sum()


def yearly_attack_by_country(df: DataFrame) -> Series:
    return df.groupby(["country", "year"]).size()


def pct_change_by_year(series: Series) -> Series:
    return series.groupby(["country"]).pct_change().round(3) * 100


def yearly_attack_pct_change_by_country(df: DataFrame) -> Series:
    return pipe(
        yearly_attack_by_country(df),
        pct_change_by_year
    )


def active_groups_by_country(df: DataFrame) -> Series:
    return df.groupby(["country", "group_name"]).size()

