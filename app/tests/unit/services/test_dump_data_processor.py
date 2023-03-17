import copy
import json
import os.path

import pytest

from src.services.dump_data_processor import data_sift, write_github_user_file
from tests.conftest import invalid_basic_types


# -------------------- data_sift() --------------------------------
def test_data_sifting_correctly(data_grouped, data_sifted):
    # Test that the function sift correctly the input data
    data_sifted_test = data_sift(data_grouped)

    assert data_sifted_test == data_sifted


def test_raises_exception_for_missing_key_data_sift(data_grouped):
    # Test that the function raises an exception if the input data is missing some key
    invalid_data_grouped = copy.deepcopy(data_grouped)
    invalid_data_grouped[0].pop("login")

    with pytest.raises(KeyError):
        data_sift(invalid_data_grouped)


@pytest.mark.parametrize("invalid_basic_types", invalid_basic_types)
def test_raises_exception_invalid_input_data_sift(invalid_basic_types):
    # Test that the function raises an exception if the input data is invalid

    with pytest.raises((KeyError, IndexError, TypeError)):
        data_sift(invalid_basic_types)


# -------------------- write_github_user_file() --------------------
def test_writes_file_with_correct_name(valid_input_write_github_user_file):
    # Test that the function writes a file with the correct name
    write_github_user_file(valid_input_write_github_user_file)

    file_name = (
        valid_input_write_github_user_file["name"].replace(" ", "").lower()
        + ".txt"
    )
    assert os.path.isfile(file_name)
    os.remove(file_name)


def test_writes_file_with_correct_data(valid_input_write_github_user_file):
    # Test that the function writes a file with the correct data
    write_github_user_file(valid_input_write_github_user_file)

    file_name = (
        valid_input_write_github_user_file["name"].replace(" ", "").lower()
        + ".txt"
    )

    with open(file_name, "r") as f:
        data_loaded = f.read()
        data_dicted = json.loads(data_loaded.replace("'", '"'))
        assert data_dicted == valid_input_write_github_user_file
    os.remove(file_name)


def test_raises_exception_for_missing_key_write_github_user_file(
    valid_input_write_github_user_file,
):
    # Test that the function raises an exception if the input data is missing some key
    invalid_input_write_github_user_file = copy.deepcopy(
        valid_input_write_github_user_file
    )
    invalid_input_write_github_user_file.pop("login")

    with pytest.raises(KeyError):
        write_github_user_file(invalid_input_write_github_user_file)


@pytest.mark.parametrize("invalid_basic_types", invalid_basic_types)
def test_raises_exception_invalid_input_write_github_user_file(
    invalid_basic_types,
):
    # Test that the function raises an exception if the input data is invalid

    with pytest.raises((KeyError, IndexError, TypeError)):
        write_github_user_file(invalid_basic_types)


# TODO: permission_error
# def test_raises_exception_for_permission_error(valid_input_write_github_user_file):
# Test that the function raises an exception if there is a permission error when writing the file
#   ...
