from dataclasses import dataclass
from typing import Dict, List


@dataclass
class UserBasicData:
    user_basic_data: Dict[str, str | int | bool | None]

    def __post_init__(self):
        assert isinstance(self.user_basic_data, Dict)
        assert all(
            isinstance(value, (str, int, bool, type(None)))
            for value in self.user_basic_data.values()
        )


@dataclass
class Repository:
    repository: Dict[str, str | int | bool | Dict | None | List]

    def __post_init__(self):
        assert isinstance(self.repository, Dict)

        for key, value in self.repository.items():
            assert isinstance(key, str)
            assert isinstance(value, (str, int, bool, dict, type(None), list))


@dataclass
class UserRepositories:
    repositories: List[Dict[str, str | int | bool | Dict | None | List]]

    def __init__(self, repositories):
        assert isinstance(repositories, List), "repositories must be a list"
        assert all(
            isinstance(repo, Dict) for repo in repositories), "each repository must be a dictionary"
        self.repositories = [Repository(repo) for repo in repositories]


@dataclass
class GroupedUserData:
    user_data: UserBasicData
    user_repositories: UserRepositories

    def __post_init__(self):
        assert isinstance(self.user_data, UserBasicData)
        assert isinstance(self.user_repositories, UserRepositories)


@dataclass
class FilteredData:
    data: Dict[str, str | int | List]

    def __post_init__(self):
        assert isinstance(self.data, Dict)
        assert all(
            isinstance(value, (str, int, List)) for value in self.data.values()
        )
