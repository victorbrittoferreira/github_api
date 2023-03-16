import json
from src.use_cases.github_profile_processor import GitHubProfileProcessor
import os.path

# fazer um schema
# def test_group_user_data(data_grouped):
#     test = GitHubProfileProcessor('victorbrittoferreira')
#     test2 = test.group_user_data()

#     assert test2 == data_grouped


def test_dump_user_data(data_grouped):
    test = GitHubProfileProcessor('test')
    GitHubProfileProcessor.user_data = data_grouped
    test.dump_user_data()

    file_name = f"{data_grouped[0]['login']}.txt"
    assert os.path.isfile(file_name)
    os.remove(file_name)


def test_data_dump_user_data(data_grouped, data_sifted):
    test = GitHubProfileProcessor('test')
    GitHubProfileProcessor.user_data = data_grouped
    test.dump_user_data()
    file_name = f"{data_grouped[0]['login']}.txt"
    with open(file_name, 'r') as f:
        data_loaded = f.read()
        data_dicted = json.loads(data_loaded.replace("'", '"'))

    os.remove(file_name)
