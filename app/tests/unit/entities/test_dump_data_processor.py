import json
import os.path
from dataclasses import asdict

import pytest
from pytest_mock import mocker

from src.entities.dump_data_processor import GitProfileDumperToFile
from src.use_cases.exception import GitProfileDataDumperError


# -------------------- GitProfileDumperToFile.extract_user_summary() ---------
def test_valid_extract_user_summary(grouped_user_data, valided_filtered_data):
    # Test that the function sift correctly the input data
    git_profile_dumper_to_profile = GitProfileDumperToFile(grouped_user_data)

    valid_output = git_profile_dumper_to_profile.extract_user_summary()
    assert valid_output == valided_filtered_data


# -------------------- GitProfileDumperToFile.dump_user_data() ----------------
def test_writes_file_dump_user_data(grouped_user_data):
    # Test that the function writes a file with the correct name
    git_profile_dumper_to_profile = GitProfileDumperToFile(grouped_user_data)
    git_profile_dumper_to_profile.extract_user_summary()
    git_profile_dumper_to_profile.dump_user_data()

    file_name = (
        grouped_user_data.user_data.user_basic_data["name"]
        .replace(" ", "")
        .lower()
        + ".txt"
    )
    assert os.path.isfile(file_name)
    os.remove(file_name)


def test_writes_file_with_correct_data(
    grouped_user_data, valided_filtered_data
):
    # Test that the function writes a file with the correct data
    git_profile_dumper_to_profile = GitProfileDumperToFile(grouped_user_data)
    git_profile_dumper_to_profile.extract_user_summary()
    git_profile_dumper_to_profile.dump_user_data()

    file_name = (
        grouped_user_data.user_data.user_basic_data["name"]
        .replace(" ", "")
        .lower()
        + ".txt"
    )

    with open(file_name, "r", encoding="utf-8") as file:
        data_loaded = file.read()
        data_dicted = json.loads(data_loaded.replace("'", '"'))
        assert data_dicted == asdict(valided_filtered_data)["data"]
    os.remove(file_name)


def test_raises_dump_user_data_with_error(grouped_user_data, mocker):
    # Create an instance of the class being tested
    git_profile_dumper_to_profile = GitProfileDumperToFile(grouped_user_data)
    git_profile_dumper_to_profile.extract_user_summary()
    file_name = (
        grouped_user_data.user_data.user_basic_data["name"]
        .replace(" ", "")
        .lower()
        + ".txt"
    )

    # Mock the behavior of the open function to raise an OSError
    mocker.patch("builtins.open", side_effect=OSError("Mock OSError"))

    # Call the method being tested and verify that it raises a GitProfileDataDumperError
    with pytest.raises(GitProfileDataDumperError):
        git_profile_dumper_to_profile.dump_user_data()

    # Verify that no file was created
    assert not os.path.exists(f"./{file_name}")
