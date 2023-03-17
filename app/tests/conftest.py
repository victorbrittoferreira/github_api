import pytest

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
def valid_username():
    return "victorbrittoferreira"


@pytest.fixture(scope="function")
def valid_username_id():
    return 34899711


@pytest.fixture(scope="function")
def valid_input_write_github_user_file():
    return {
        "login": "victorbrittoferreira",
        "name": "Victor Britto Ferreira",
        "url": "https://api.github.com/users/victorbrittoferreira",
        "public_repositories": 27,
        "followers": 8,
        "following": 12,
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
            "zsh-autosuggestions",
        ],
    }


@pytest.fixture(scope="function")
def data_grouped():
    return (
        {
            "login": "victorbrittoferreira",
            "name": "Victor Britto Ferreira",
            "url": "https://api.github.com/users/victorbrittoferreira",
            "public_repos": 27,
            "followers": 8,
            "following": 12,
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
            {"name": "zsh-autosuggestions"},
        ],
    )


@pytest.fixture(scope="function")
def data_sifted():
    return {
        "login": "victorbrittoferreira",
        "name": "Victor Britto Ferreira",
        "url": "https://api.github.com/users/victorbrittoferreira",
        "public_repositories": 27,
        "followers": 8,
        "following": 12,
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
            "zsh-autosuggestions",
        ],
    }
