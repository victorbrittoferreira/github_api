from dataclasses import asdict
import json
import os.path

from src.main import extract_github_user_profile


def test_successfully_extract_github_user_profile(
    valid_username, valided_filtered_data, github_personal_access_token_
):
    # Test that the function has expected behavior.
    extract_github_user_profile(valid_username, github_personal_access_token_)

    with open(f"{valid_username}.txt", "r", encoding="utf-8") as file:
        data_loaded = file.read()
        data_dicted = json.loads(data_loaded.replace("'", '"'))

        assert data_dicted == asdict(valided_filtered_data)['data']

    os.remove(f"{valid_username}.txt")
