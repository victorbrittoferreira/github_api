import requests
from requests.exceptions import HTTPError


def ask_user():
    # return str(input("Input username:"))
    return 'victorbrittoferreira'


# user_name = ask_user()

# TODO: colocar um async e exception customizada


def request_github(user_name):
    url = f"https://api.github.com/users/{user_name}"
    url_repo = f'https://api.github.com/users/{user_name}/repos'
    try:
        requests_user = (url, url_repo)
        user_repo_data = []
        for url in requests_user:
            response = requests.get(url)
            if response.status_code == 200:
                user_repo_data.append(response.json())
            else:
                response.raise_for_status()
    except HTTPError:
        raise
    return user_repo_data


# user_data = request_github(user_name)

# TODO: colocar exception customizada


def collect_user_summary(user_data):
    try:
        user_summary = (
            user_data['name'], user_data['url'], user_data['public_repos'],
            user_data['followers'], user_data['following']
        )
    except KeyError:
        raise
    return user_summary


# user_summary = collect_user_summary(user_data[0])


# TODO: colocar exception customizada
def collect_user_repositories(repositories):
    try:
        list_repo = [repo['name'] for repo in repositories]
    except KeyError:
        raise
    return tuple(list_repo)


# repository_list = collect_user_repositories(user_data[1])


def data_dump_to_txt(user_summary: tuple, repository_list: tuple) -> None:
    try:
        with open('github_user_dossier.txt', 'w') as f:
            f.write(
                f"{user_summary[0]}, {user_summary[1]}, {user_summary[2]},"
                f" {user_summary[3]}, {user_summary[4]}, {repository_list}"
            )
    except IndexError:
        raise
    return None


# data_dump_to_txt(user_summary, repository_list)
