from typing import Dict, Tuple


def data_sift(user_data: Tuple) -> Dict:
    try:
        user_summary = {
            "name": user_data[0]["name"],
            "url": user_data[0]["url"],
            "public_repositories": user_data[0]["public_repos"],
            "followers": user_data[0]["followers"],
            "following": user_data[0]["following"],
            "repositories_name_list": [
                repository["name"] for repository in user_data[1]
            ],
        }
    except KeyError:
        raise

    return user_summary


def write_github_user_file(github_user_data: Dict) -> None:
    file_name = f"{github_user_data['name'].replace(' ','_').lower()}.txt"
    with open(file_name, "w") as _file:
        _file.write(str(github_user_data))
