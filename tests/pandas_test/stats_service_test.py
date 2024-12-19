import app.pandas_.stats_service as stats_service

def test_total_damage_by_attack_type(terror_attacks_df):
    res = stats_service.total_damage_by_attack_type(terror_attacks_df)
    assert res.iloc[0] == 98


def test_avg_damage_by_country(terror_attacks_df):
    res = stats_service.avg_damage_by_country(terror_attacks_df)
    assert res.iloc[0] == 0.957


def test_total_damage_by_group(terror_attacks_df):
    res = stats_service.total_damage_by_group(terror_attacks_df)
    assert res.iloc[6] == 10


def test_yearly_attack_by_country(terror_attacks_df):
    res = stats_service.yearly_attack_by_country(terror_attacks_df)
    assert res.iloc[0] == 21


def test_pct_change_by_year(terror_attacks_df):
    terror_attack_series = stats_service.yearly_attack_by_country(terror_attacks_df)
    res = stats_service.pct_change_by_year(terror_attack_series)
    assert res.iloc[1] == -66.7



def test_yearly_attack_pct_change_by_country(terror_attacks_df):
    res = stats_service.yearly_attack_pct_change_by_country(terror_attacks_df)
    assert res.iloc[5] == 100


def test_active_groups_by_country(terror_attacks_df):
    res = stats_service.active_groups_by_country(terror_attacks_df)
    assert res.iloc[0] == 3
