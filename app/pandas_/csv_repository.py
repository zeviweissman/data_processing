from typing import List
import pandas as pd
from pandas import DataFrame
from toolz import pipe
from toolz.curried import partial

from app.pandas_.csv_read_settings import global_terrorism_csv_read_settings


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


def get_global_terrorism_as_dict() -> List[dict]:
    return pipe(
        csv_to_df(global_terrorism_csv_read_settings),
        partial(rename_columns, columns_to_rename=global_terrorism_csv_read_settings['columns_to_rename']),
        partial(fill_null_columns, columns_to_fill=global_terrorism_csv_read_settings['columns_to_fill']),
        add_deadly_score,
        df_to_dict
    )


def get_global_terrorism_as_df() -> DataFrame:
    return pipe(
        csv_to_df(global_terrorism_csv_read_settings),
        partial(rename_columns, columns_to_rename=global_terrorism_csv_read_settings['columns_to_rename']),
        partial(fill_null_columns, columns_to_fill=global_terrorism_csv_read_settings['columns_to_fill']),
        add_deadly_score
    )

