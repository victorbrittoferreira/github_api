import requests
from requests.exceptions import HTTPError
from typing import Generator, Iterable, Tuple


# TODO: colocar um async e exception customizada

def url_format(user_name: str, url_user: str, url_user_repo: str) -> Tuple[str, str]:
    named_url_user = url_user.replace('user_name', user_name)
    named_url_user_repo = url_user_repo.replace('user_name', user_name)

    return named_url_user, named_url_user_repo


def request_github(url_user: str, url_user_repo: str) -> Tuple[dict, list]:
    try:
        requests_user = (url_user, url_user_repo)
        user_repo_data = []
        for url in requests_user:
            response = requests.get(url)
            if response.status_code == 200:
                user_repo_data.append(response.json())
            else:
                response.raise_for_status()
    except HTTPError:
        raise
    return tuple(user_repo_data)


# TODO: colocar exception customizada


def collect_user_summary(user_data: dict) -> Tuple[str | int]:
    try:
        user_summary = (
            user_data["name"],
            user_data["url"],
            user_data["public_repos"],
            user_data["followers"],
            user_data["following"],
        )
    except KeyError:
        raise
    return user_summary


# TODO: colocar exception customizada
def collect_user_repositories(repositories: list) -> Generator[int, str, Iterable]:
    try:
        list_repo = (repo["name"] for repo in repositories)
    except KeyError:
        raise
    return list_repo


def data_dump_to_txt(user_summary: tuple, repository_list: tuple) -> None:
    try:
        with open("github_user_dossier.txt", "w") as f:
            f.write(
                f"{user_summary[0]}, {user_summary[1]}, {user_summary[2]},"
                f" {user_summary[3]}, {user_summary[4]}, {[*repository_list]}"
            )
    except IndexError:
        raise
    return None
