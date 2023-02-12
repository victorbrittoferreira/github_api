import requests


def ask_user():
    # return str(input("Input username:"))
    return 'victorbrittoferreira'


user_name = ask_user()


def request_github(user_name):
    try:
        user_repo_data = []
        url = f"https://api.github.com/users/{user_name}"
        url_repo = f'https://api.github.com/users/{user_name}/repos'
        requests_user = (url, url_repo)
        for url in requests_user:
            response = requests.get(url).json()
            user_repo_data.append(response)
    except:
        ...
    return user_repo_data


user_data = request_github(user_name)


def collect_user_summary(user_data):
    user_sumary = (
        user_data['name'], user_data['url'], user_data['public_repos'],
        user_data['followers'], user_data['following']
    )

    return user_summary


user_summary = collect_user_summary(user_data[0])


def collect_user_repositories(repositories):
    list_repo = []
    for repo in repositories:
        list_repo.append(repo['name'])

    return list_repo


repository_list = collect_user_repositories(user_data[1])


def data_dump_to_txt(user_summary, repositories_list):
    with open('test.txt', 'w') as f:
        f.write(
            f"{user_summary[0]}, {user_summary[1]}, {user_summary[2]},"
            f" {user_summary[3]}, {user_summary[4]}, {user_summary[5]},"
            f" {repositories_list}"
        )
