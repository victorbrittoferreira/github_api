from main import (
    url_format,
    collect_user_repositories,
    collect_user_summary,
    data_dump_to_txt,
    request_github,
)
from config import UserGithubDossierConfig

if __name__ == "__main__":
    named_urls = url_format(
        UserGithubDossierConfig.USER_NAME,
        UserGithubDossierConfig.URL_USER,
        UserGithubDossierConfig.URL_USER_REPO)
    user_data = request_github(*named_urls)
    user_summary = collect_user_summary(user_data[0])
    repository_list = collect_user_repositories(user_data[1])
    data_dump_to_txt(user_summary, repository_list)

    print("Terminou")
