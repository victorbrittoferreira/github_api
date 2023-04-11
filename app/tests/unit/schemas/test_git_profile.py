from dataclasses import asdict

import pytest

from src.schemas.git_profile import (
    FilteredData,
    GroupedUserData,
    Repository,
    UserBasicData,
    UserRepositories,
)


# ---------------------------------- UserBasicData ---------------------------
def test_valid_user_basic_data():
    """
    Test creating a valid UserBasicData object with valid data.
    """
    data = {"name": "John", "age": 42, "is_active": True, "address": None}
    user_data = UserBasicData(user_basic_data=data)

    assert asdict(user_data) == {"user_basic_data": data}


def test_invalid_value_user_basic_data():
    """
    Test creating a UserBasicData object with invalid data.
    """
    data = {"name": "John", "age": 42, "is_active": (), "address": None}
    with pytest.raises(AssertionError):
        UserBasicData(user_basic_data=data)


def test_empty_user_basic_data():
    """
    Test creating a UserBasicData object with an empty dictionary.
    """
    data = {}
    user_data = UserBasicData(user_basic_data=data)

    assert asdict(user_data) == {"user_basic_data": {}}


# ---------------------------------- Repository ---------------------------
def test_valid_repository():
    """
    Test creating a valid Repository object with valid data.
    """
    repository = Repository(
        {
            "name": "test_repo",
            "id": 123,
            "is_private": True,
            "metadata": {
                "owner": "John Doe",
                "description": "A test repository",
            },
            "tags": ["test", "repository"],
        }
    )
    assert isinstance(repository, Repository)


def test_invalid_repository():
    """
    Test creating a Repository object with invalid data.
    """
    with pytest.raises(AssertionError):
        Repository(
            {
                "name": "test_repo",
                "id": 123,
                "is_private": (),
                "metadata": {
                    "owner": "John Doe",
                    "description": "A test repository",
                },
                "tags": ["test", "repository"],
                "extra_field": "this should not be here",
            }
        )


def test_empty_repository():
    """
    Test creating a Repository object with an empty dictionary.
    """
    data = {}
    user_repository = Repository(repository=data)

    assert asdict(user_repository) == {"repository": {}}


# ------------------------------ UserRepositories ---------------------------
def test_valid_user_repositories():
    """
    Test creating a valid UserRepositories object with valid data.
    """
    repo1 = {"name": "repo1", "id": 123, "tags": ["tag1", "tag2"]}
    repo2 = {"name": "repo2", "id": 456, "tags": ["tag3", "tag4"]}
    user_repos = UserRepositories(repositories=[repo1, repo2])
    assert user_repos is not None


def test_invalid_user_repositories():
    """
    Test creating a UserRepositories object with invalid data.
    """
    repo1 = Repository(
        {"name": "repo1", "id": "invalid_id", "tags": ["tag1", "tag2"]}
    )
    repo2 = ""
    with pytest.raises(AssertionError):
        UserRepositories([repo1, repo2])


def test_empty_repositories():
    """
    Test creating a UserRepositories object with an empty list.
    """
    data = []
    user_repositories = UserRepositories(repositories=data)

    assert asdict(user_repositories) == {"repositories": []}


# ------------------------------ GroupedUserData ---------------------------
def test_valid_grouped_user_data():
    """
    Test creating a valid GroupedUserData object with valid UserBasicData and
    UserRepositories objects.
    """
    user_basic_data = UserBasicData(
        {"username": "johndoe", "age": 30, "active": True}
    )

    repo1 = {"name": "repo1", "id": 123, "tags": ["tag1", "tag2"]}
    repo2 = {"name": "repo2", "id": 456, "tags": ["tag3", "tag4"]}
    repositories = [repo1, repo2]

    user_repositories = UserRepositories(repositories)
    grouped_user_data = GroupedUserData(user_basic_data, user_repositories)
    assert isinstance(grouped_user_data, GroupedUserData)

    assert grouped_user_data.user_data == user_basic_data
    assert grouped_user_data.user_repositories == user_repositories


def test_invalid_grouped_user_data():
    """
    Test creating a GroupedUserData object with invalid data.
    """
    user_basic_data = UserBasicData(
        {"username": "johndoe", "age": 30, "active": True}
    )
    with pytest.raises(AssertionError):
        GroupedUserData(user_basic_data, [])


def test_empty_grouped_user_data():
    """
    Test creating a GroupedUserData object with an empty dictionary and an empty list.
    """
    user_basic_data = {}
    repo1 = []

    user_repositories = UserRepositories(repositories=repo1)
    with pytest.raises(AssertionError):
        GroupedUserData(user_basic_data, user_repositories)


# -------------------------------- FilteredData ----------------------------
def test_valid_filtered_data():
    """
    Test creating a valid FilteredData object with valid data.
    """
    data_test = {"name": "John", "age": 42, "test": [1, 2]}
    user_filtered_data = FilteredData(data=data_test)

    assert asdict(user_filtered_data) == {"data": data_test}


def test_invalid_filtered_data():
    """
    Test creating a FilteredData object with invalid data.
    """
    data_test = {"name": "John", "age": 42, "is_active": (), "address": None}
    with pytest.raises(AssertionError):
        FilteredData(data=data_test)


def test_empty_filtered_data():
    """
    Test creating a FilteredData object with an empty dictionary.
    """
    data_test = {}
    user_filtered_data = FilteredData(data=data_test)

    assert asdict(user_filtered_data) == {"data": {}}
