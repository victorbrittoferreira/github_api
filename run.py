from main import (
    ask_user, collect_user_repositories, collect_user_summary, data_dump_to_txt, request_github,)

import os
from os.path import dirname, join
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


if __name__ == "__main__":
    user_name = ask_user()
    user_data = request_github(user_name)
    user_summary = collect_user_summary(user_data[0])
    repository_list = collect_user_repositories(user_data[1])
    data_dump_to_txt(user_summary, repository_list)

    print("Terminou")
