import app.db.postgres.repository.group_repository as group_repos


def insert_groups(groups: set):
    for group in groups:
        group_repos.getsert_groups(group)


def get_dict_of_key_group_value_group_id():
    return {group.name : group.id for group in group_repos.get_groups()}