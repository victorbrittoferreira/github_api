import json
import os.path

from src.schemas.git_profile import GroupedUserData
from src.use_cases.github_profile_processor import GitProfileProcessor


# -------------------- GitProfileProcessor.group_user_data() -----------------------
def test_valid_return_group_user_data(
    valid_username,
    github_personal_access_token_,
    github_client,
    git_profile_dumper_to_file,
):
    # Test that the method valid data return
    profile_processor = GitProfileProcessor(
        valid_username,
        github_personal_access_token_,
        github_client,
        git_profile_dumper_to_file,
    )
    profile_processor.group_user_data()

    assert isinstance(profile_processor._user_raw_data, GroupedUserData)


# -------------------- GitProfileProcessor.dump_user_data() -----------------------
def test_create_file_name(
    valid_username,
    github_personal_access_token_,
    github_client,
    git_profile_dumper_to_file,
    grouped_user_data,
):
    # Test that the method create correct name txt file
    profile_processor = GitProfileProcessor(
        valid_username,
        github_personal_access_token_,
        github_client,
        git_profile_dumper_to_file,
    )

    # GitProfileProcessor.user_data = grouped_user_data
    profile_processor._user_raw_data = grouped_user_data

    profile_processor.dump_user_data()

    file_name = f"{valid_username}.txt"
    assert os.path.exists(file_name)
    os.remove(file_name)


def test_correct_user_data_dump_file(
    valid_username,
    github_personal_access_token_,
    github_client,
    git_profile_dumper_to_file,
    grouped_user_data,
    filtered_data,
):
    # Test that the method dump correct user data in txt file
    profile_processor = GitProfileProcessor(
        valid_username,
        github_personal_access_token_,
        github_client,
        git_profile_dumper_to_file,
    )
    profile_processor._user_raw_data = grouped_user_data

    profile_processor.dump_user_data()

    file_name = f"{valid_username}.txt"
    with open(file_name, "r", encoding="utf-8") as file:
        data_loaded = file.read()
        data_dicted = json.loads(data_loaded.replace("'", '"'))

        assert data_dicted == filtered_data
    os.remove(file_name)
