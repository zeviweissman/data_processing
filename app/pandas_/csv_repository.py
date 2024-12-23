from datetime import timedelta
from typing import List
import pandas as pd
from pandas import DataFrame, Timestamp
from toolz import pipe
from toolz.curried import partial
from app.pandas_.csv_read_settings import extended_global_terrorism_csv_read_settings, global_terrorism_csv_read_settings


def csv_to_df(settings: dict) -> DataFrame:
    return pd.read_csv(filepath_or_buffer=settings['csv_path'], usecols=settings['columns_to_read'],
                       dtype=settings['dtypes'], encoding='latin-1',
                       low_memory=False)


def rename_columns(df: DataFrame, columns_to_rename: dict) -> DataFrame:
    return df.rename(columns=columns_to_rename)


def fill_null_columns(df: DataFrame, columns_to_fill: dict) -> DataFrame:
    return df.fillna(columns_to_fill)


def add_deadly_score(df: DataFrame) -> DataFrame:
    return df.assign(deadly_score=(df['total_wounded'].where(df['total_wounded'] >= 0)
                                   + (df["total_killed"].where(df["total_killed"] >= 0) * 2))).fillna(-1)


def df_to_dict(df: DataFrame) -> List[dict]:
    return df.to_dict(orient='records')

def convert_date_dtypes(df: DataFrame) -> DataFrame:
    return df

def parse_year_day_month_to_date_column(df: DataFrame) -> DataFrame:
    return df.assign(date=pd.to_datetime(df[["year", "month", "day"]], errors='coerce'))



def parse_date_txt_to_date_column(df: DataFrame) -> DataFrame:
    return df.assign(date=pd.to_datetime(df['Date'], errors='coerce'))

def correct_century(str_date: Timestamp) -> str:
    return str_date - pd.DateOffset(years=100) if str_date > Timestamp("2025-01-01") else str_date

def correct_date_century(df: DataFrame) -> DataFrame:
    return df.assign(date=[correct_century(date) for date in df['date']])

def parse_date_txt_column_with_correct_century(df: DataFrame) -> DataFrame:
    return pipe(
        df,
        parse_date_txt_to_date_column,
        correct_date_century
    )




def get_extended_global_terrorism_as_df() -> DataFrame:
    return pipe(
        csv_to_df(extended_global_terrorism_csv_read_settings),
        partial(rename_columns, columns_to_rename=extended_global_terrorism_csv_read_settings['columns_to_rename']),
        partial(fill_null_columns, columns_to_fill=extended_global_terrorism_csv_read_settings['columns_to_fill']),
        add_deadly_score,
        parse_year_day_month_to_date_column
    )

def get_global_terrorism_as_df() -> DataFrame:
    return pipe(
        csv_to_df(global_terrorism_csv_read_settings),
        partial(rename_columns, columns_to_rename=global_terrorism_csv_read_settings['columns_to_rename']),
        partial(fill_null_columns, columns_to_fill=global_terrorism_csv_read_settings['columns_to_fill']),
        parse_date_txt_column_with_correct_century
    )

def concat_dfs(dfs: List[DataFrame]) -> DataFrame:
    return pd.concat(dfs, ignore_index=True, join="inner")

def remove_duplicates_from_merged_df(df: DataFrame) -> DataFrame:
    return df.drop_duplicates()


def merge_same_attacks(df: DataFrame) -> DataFrame:
    return df.groupby(['date', 'city', 'country', 'group_name']).agg({"total_wounded": "max", "total_killed": "max",  "attack_type": set, "description": list}).reset_index()




global_terrorism_df = get_global_terrorism_as_df()
extended_global_terrorism_df = get_extended_global_terrorism_as_df()
global_terrorism_dict = df_to_dict(global_terrorism_df)
extended_global_terrorism_dict = df_to_dict(extended_global_terrorism_df)

merged_terrorism_dict = pipe(
    concat_dfs([global_terrorism_df, extended_global_terrorism_df]),
    remove_duplicates_from_merged_df,
    merge_same_attacks,
    df_to_dict
)
