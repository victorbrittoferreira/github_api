import json
import os.path

from src.use_cases.github_profile_processor import GitHubProfileProcessor

# -------------------- GitHubProfileProcessor.group_user_data() --------------------------------


def test_valid_return_group_user_data(
    data_grouped, valid_username_id, valid_username
):
    # Test that the method valid data return
    profile_processor = GitHubProfileProcessor(valid_username)
    grouped_user_data = profile_processor.group_user_data()

    repository_name = grouped_user_data[1][0]["name"]

    assert repository_name in [
        repository["name"] for repository in data_grouped[1]
    ]
    assert grouped_user_data[0]["id"] == valid_username_id


def test_valid_return_data_structure_group_user_data(valid_username):
    # Test that the method valid data structure
    profile_processor = GitHubProfileProcessor(valid_username)

    result = profile_processor.group_user_data()

    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], dict)
    assert isinstance(result[1], list)


# -------------------- GitHubProfileProcessor.dump_user_data() --------------------------------
def test_create_file_name(data_grouped):
    # Test that the method create correct name txt file
    profile_processor = GitHubProfileProcessor("test")
    GitHubProfileProcessor.user_data = data_grouped
    profile_processor.dump_user_data()

    file_name = f"{data_grouped[0]['login']}.txt"
    assert os.path.exists(file_name)
    os.remove(file_name)


def test_correct_user_data_dump_file(data_grouped, data_sifted):
    # Test that the method dump correct user data in txt file
    profile_processor = GitHubProfileProcessor("test")
    GitHubProfileProcessor.user_data = data_grouped

    profile_processor.dump_user_data()

    file_name = f"{data_grouped[0]['login']}.txt"
    with open(file_name, "r") as f:
        data_loaded = f.read()
        data_dicted = json.loads(data_loaded.replace("'", '"'))
        del data_sifted["login"]

        assert data_dicted == data_sifted
    os.remove(file_name)
