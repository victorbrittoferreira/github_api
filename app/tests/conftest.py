import pytest

from config import ConfigApp
from src.entities.dump_data_processor import GitProfileDumperToFile
from src.entities.github_api_client import GitHubClient
from src.schemas.git_profile import (
    FilteredData,
    GroupedUserData,
    Repository,
    UserBasicData,
    UserRepositories,
)

invalid_basic_types = [
    "string",
    2,
    1.2,
    "",
    (),
    [],
    {},
    set([]),
    frozenset({}),
    lambda: "function",
    type("MyClass", (object,), {}),
    None,
    False,
]


@pytest.fixture(scope="function")
def github_personal_access_token_():
    return ConfigApp.GITHUB_PERSONAL_ACCESS_TOKEN


@pytest.fixture(scope="function")
def valid_username():
    return "victorbrittoferreira"


@pytest.fixture(scope="function")
def valid_username_id():
    return 34899711


@pytest.fixture(scope="function")
def github_client():
    return GitHubClient()


@pytest.fixture(scope="function")
def git_profile_dumper_to_file():
    return GitProfileDumperToFile()


@pytest.fixture(scope="function")
def basic_data_user():
    return (
        {
            "name": "Victor Britto Ferreira",
            "url": "https://api.github.com/users/victorbrittoferreira",
            "public_repos": 26,
            "followers": 8,
            "following": 14,
        },
    )


@pytest.fixture(scope="function")
def repositories():
    return (
        [
            {"name": "angular_todo_list"},
            {"name": "asynchronous_python"},
            {"name": "data_manipulation"},
            {"name": "django_blog"},
            {"name": "django_test"},
            {"name": "DRF_API_test"},
            {"name": "easy-mask"},
            {"name": "exc-isquicha-training"},
            {"name": "fastapi_store"},
            {"name": "fast_api"},
            {"name": "fast_api_clothes_store"},
            {"name": "github_api"},
            {"name": "im_bank"},
            {"name": "interview_test"},
            {"name": "JOSE-PORTILLA"},
            {"name": "jsReload"},
            {"name": "mechanical-keyboard"},
            {"name": "newMoshJsBeginner"},
            {"name": "pandas"},
            {"name": "product_hunt"},
            {"name": "PY-STDY"},
            {"name": "requests-futures"},
            {"name": "spreadsheet_db"},
            {"name": "web_encoder"},
            {"name": "Word-Counter"},
            {"name": "wordcount_project"},
        ],
    )


@pytest.fixture(scope="function")
def data_grouped():
    return (
        {
            "name": "Victor Britto Ferreira",
            "url": "https://api.github.com/users/victorbrittoferreira",
            "public_repos": 26,
            "followers": 8,
            "following": 14,
        },
        [
            {"name": "angular_todo_list"},
            {"name": "asynchronous_python"},
            {"name": "data_manipulation"},
            {"name": "django_blog"},
            {"name": "django_test"},
            {"name": "DRF_API_test"},
            {"name": "easy-mask"},
            {"name": "exc-isquicha-training"},
            {"name": "fastapi_store"},
            {"name": "fast_api"},
            {"name": "fast_api_clothes_store"},
            {"name": "github_api"},
            {"name": "im_bank"},
            {"name": "interview_test"},
            {"name": "JOSE-PORTILLA"},
            {"name": "jsReload"},
            {"name": "mechanical-keyboard"},
            {"name": "newMoshJsBeginner"},
            {"name": "pandas"},
            {"name": "product_hunt"},
            {"name": "PY-STDY"},
            {"name": "requests-futures"},
            {"name": "spreadsheet_db"},
            {"name": "web_encoder"},
            {"name": "Word-Counter"},
            {"name": "wordcount_project"},
        ],
    )


@pytest.fixture(scope="function")
def grouped_user_data():
    basic_data_user = {
        "name": "Victor Britto Ferreira",
        "url": "https://api.github.com/users/victorbrittoferreira",
        "public_repos": 26,
        "followers": 8,
        "following": 14,
    }
    repositories = [
        {"name": "angular_todo_list"},
        {"name": "asynchronous_python"},
        {"name": "data_manipulation"},
        {"name": "django_blog"},
        {"name": "django_test"},
        {"name": "DRF_API_test"},
        {"name": "easy-mask"},
        {"name": "exc-isquicha-training"},
        {"name": "fastapi_store"},
        {"name": "fast_api"},
        {"name": "fast_api_clothes_store"},
        {"name": "github_api"},
        {"name": "im_bank"},
        {"name": "interview_test"},
        {"name": "JOSE-PORTILLA"},
        {"name": "jsReload"},
        {"name": "mechanical-keyboard"},
        {"name": "newMoshJsBeginner"},
        {"name": "pandas"},
        {"name": "product_hunt"},
        {"name": "PY-STDY"},
        {"name": "requests-futures"},
        {"name": "spreadsheet_db"},
        {"name": "web_encoder"},
        {"name": "Word-Counter"},
        {"name": "wordcount_project"},
    ]
    validated_basic_data_user = UserBasicData(basic_data_user)

    validated_repositories = UserRepositories(repositories)
    grouped_user_data_ = GroupedUserData(
        validated_basic_data_user, validated_repositories
    )

    return grouped_user_data_


@pytest.fixture(scope="function")
def filtered_data():
    return {
        "name": "Victor Britto Ferreira",
        "url": "https://api.github.com/users/victorbrittoferreira",
        "public_repositories": 26,
        "followers": 8,
        "following": 14,
        "repositories_name_list": [
            "angular_todo_list",
            "asynchronous_python",
            "data_manipulation",
            "django_blog",
            "django_test",
            "DRF_API_test",
            "easy-mask",
            "exc-isquicha-training",
            "fastapi_store",
            "fast_api",
            "fast_api_clothes_store",
            "github_api",
            "im_bank",
            "interview_test",
            "JOSE-PORTILLA",
            "jsReload",
            "mechanical-keyboard",
            "newMoshJsBeginner",
            "pandas",
            "product_hunt",
            "PY-STDY",
            "requests-futures",
            "spreadsheet_db",
            "web_encoder",
            "Word-Counter",
            "wordcount_project",
        ],
    }


@pytest.fixture(scope="function")
def valided_filtered_data():
    filtered_data = {
        "name": "Victor Britto Ferreira",
        "url": "https://api.github.com/users/victorbrittoferreira",
        "public_repositories": 26,
        "followers": 8,
        "following": 14,
        "repositories_name_list": [
            "angular_todo_list",
            "asynchronous_python",
            "data_manipulation",
            "django_blog",
            "django_test",
            "DRF_API_test",
            "easy-mask",
            "exc-isquicha-training",
            "fastapi_store",
            "fast_api",
            "fast_api_clothes_store",
            "github_api",
            "im_bank",
            "interview_test",
            "JOSE-PORTILLA",
            "jsReload",
            "mechanical-keyboard",
            "newMoshJsBeginner",
            "pandas",
            "product_hunt",
            "PY-STDY",
            "requests-futures",
            "spreadsheet_db",
            "web_encoder",
            "Word-Counter",
            "wordcount_project",
        ],
    }
    valided_filtered_data_ = FilteredData(filtered_data)

    return valided_filtered_data_
