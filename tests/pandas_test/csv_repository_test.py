def test_csv_reading(terror_attacks_df):
    assert list(terror_attacks_df.columns) == ['year', 'month', 'day', 'country', 'region', 'province_or_state',
       'city', 'lat', 'lon', 'description','attack_type', 'target_type','group_name',
       'total_perps', 'weapon_type', 'total_killed', 'total_wounded',
       'deadly_score', 'date']
    assert terror_attacks_df.shape == (1000, 19)