from pandas import DataFrame
import pytest
from app.pandas_.csv_repository import get_extended_global_terrorism_as_df


@pytest.fixture(scope='module')
def terror_attacks_df() -> DataFrame:
    return get_extended_global_terrorism_as_df()
