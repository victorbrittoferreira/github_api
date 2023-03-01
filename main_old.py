from typing import Generator, Iterable, List, Tuple

import requests
from requests.exceptions import HTTPError

# URL_USER=https://api.github.com/users/user_name
# URL_USER_REPO=https://api.github.com/users/user_name/repos
# USER_NAME=victorbrittoferreira

"""
name: Victor Britto Ferreira
url: https://api.github.com/users/victorbrittoferreira
public_repositories: 27
followers: 8
following: 12
repositories: angular_todo_list,asynchronous_python,data_manipulation,django_blog,django_test,DRF_API_test,easy-mask,exc-isquicha-training,fastapi_store,fast_api,fast_api_clothes_store,github_api,im_bank,interview_test,JOSE-PORTILLA,jsReload,mechanical-keyboard,newMoshJsBeginner,pandas,product_hunt,PY-STDY,requests-futures,spreadsheet_db,web_encoder,Word-Counter,wordcount_project,zsh-autosuggestions
"""


# class GHProfileDataProcessor:

#     __slots__ = ("user_name", "url_user", "url_user_repo")

#     def __init__(self, user_name, url_user, url_user_repo):
#         self.user_name = user_name
#         self.url_user = url_user
#         self.url_user_repo = url_user_repo

#     @classmethod
#     def url_bulder(cls, user_name):
#         GHProfileDataProcessor.url_user =
#         GHProfileDataProcessor.url_user_repo = url_user_repo


# # TODO: colocar um async e exception customizada
# def url_format(
#     user_name: str, url_user: str, url_user_repo: str
# ) -> Tuple[str, str]:
#     named_url_user = url_user.replace("user_name", user_name)
#     named_url_user_repo = url_user_repo.replace("user_name", user_name)

#     return named_url_user, named_url_user_repo


# def request_github(url_user: str, url_user_repo: str) -> Tuple[dict, list]:
#     try:
#         requests_user = (url_user, url_user_repo)
#         user_repo_data = []
#         for url in requests_user:
#             response = requests.get(url)
#             if response.status_code == 200:
#                 user_repo_data.append(response.json())
#             else:
#                 response.raise_for_status()
#     except HTTPError:
#         raise
#     return tuple(user_repo_data)


# # TODO: colocar exception customizada
# def collect_user_summary(user_data: dict) -> Tuple[str | int]:
#     try:
#         user_summary = (
#             user_data["name"],
#             user_data["url"],
#             user_data["public_repos"],
#             user_data["followers"],
#             user_data["following"],
#         )
#     except KeyError:
#         raise
#     return user_summary


# # TODO: colocar exception customizada
# def collect_user_repositories(
#     repositories: list,
# ) -> Generator[int, str, Iterable]:
#     try:
#         list_repo = (repo["name"] for repo in repositories)
#     except KeyError:
#         raise
#     return list_repo


# def data_dump_to_txt(user_summary: tuple, repository_list: tuple) -> None:
#     try:
#         with open("github_user_dossier.txt", "w") as f:
#             f.write(
#                 f"{user_summary[0]}, {user_summary[1]}, {user_summary[2]},"
#                 f" {user_summary[3]}, {user_summary[4]}, {[*repository_list]}"
#             )
#     except IndexError:
#         raise
#     return None
