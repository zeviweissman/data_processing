import app.db.postgres.repository.attack_type_repository as attack_type_repository


def insert_attack_types(attack_types: set):
    for attack_type in attack_types:
        attack_type_repository.getsert_attack_type(attack_type)

def get_dict_of_key_attack_type_value_attack_type_id():
    return {attack_type.name : attack_type.id for attack_type in attack_type_repository.get_attack_types()}