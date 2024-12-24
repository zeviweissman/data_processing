extended_global_terrorism_csv_read_settings = {
            "csv_path": r"C:\Users\1\Desktop\final_project\data_processing\assets\globalterrorismdb_big.csv",
            "columns_to_read": ["summary","iyear", "imonth", "iday", "region_txt", "country_txt", "provstate", "city", "latitude", "longitude", "attacktype1_txt", "targtype1_txt","gname", "nperps", "weaptype1_txt", "nkill", "nwound"],
            "dtypes":
                {
                    "iyear": "Int32",
                    "imonth": "Int32",
                    "iday": "Int32",
                    "region_txt": str,
                    "country_txt": str,
                    "provstate": str,
                    "city": str,
                    "latitude": float,
                    "longitude": float,
                    "attacktype1_txt": str,
                    "targtype1_txt": str,
                    "gname": str,
                    "gname2": str,
                    "gname3": str,
                    "nperps": "Int32",
                    "weaptype1_txt": str,
                    "weaptype2_txt": str,
                    "weaptype3_txt": str,
                    "nkill": "Int32",
                    "nwound": "Int32",
                    "summary": str
                },
            "columns_to_rename":
                {
                    "iyear": "year",
                    "imonth": "month",
                    "iday": "day",
                    "provstate": "province_or_state",
                    "city": "city",
                    "region_txt": "region",
                    "country_txt": "country",
                    "latitude": "lat",
                    "longitude": "lon",
                    "attacktype1_txt": "attack_type",
                    "targtype1_txt": "target_type",
                    "gname": "group_name",
                    "nperps": "total_perps",
                    "weaptype1_txt": "weapon_type",
                    "nkill": "total_killed",
                    "nwound": "total_wounded",
                    "summary": "description"
                },
    "columns_to_fill": {
        "country": "Unknown",
        "region": "Unknown",
        "city": "Unknown",
        "province_or_state": "Unknown",
        "lat": 0.0,
        "lon": 0.0,
        "total_killed": -1,
        "total_wounded": -1,
        "total_perps": -1,
        "description": ""
    }
        }


global_terrorism_csv_read_settings = {
"csv_path": r"C:\Users\1\Desktop\final_project\data_processing\assets\terrorism_big.csv",
            "columns_to_read": ["Date", "City", "Country", "Perpetrator", "Weapon", "Injuries", "Fatalities", "Description"],
            "dtypes":
                {
                    "Date": str,
                    "City": str,
                    "Country": str,
                    "Perpetrator": str,
                    "Weapon": str,
                    "Injuries": "Int32",
                    "Fatalities": "Int32",
                    "Description": str
                },
            "columns_to_rename":
                {
                    "City": "city",
                    "Country": "country",
                    "Perpetrator": "group_name",
                    "Weapon": "attack_type",
                    "Injuries": "total_wounded",
                    "Fatalities": "total_killed",
                    "Description": "description"
                },
    "columns_to_fill": {
        "country": "Unknown",
        "city": "Unknown",
        "group_name": "Unknown",
        "attack_type": "Unknown",
        "total_killed": -1,
        "total_wounded": -1,
    }
        }


