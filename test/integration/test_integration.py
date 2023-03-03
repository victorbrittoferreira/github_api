from src.use_cases.github_profile_processor import GitHubProfileProcessor
import os.path


# def test_group_user_data(data_grouped):
#     test = GitHubProfileProcessor('victorbrittoferreira')
#     test2 = test.group_user_data()

#     assert test2 == data_grouped

    ...


def test_dump_user_data(data_grouped):
    test = GitHubProfileProcessor('test')
    GitHubProfileProcessor.user_data = data_grouped
    test.dump_user_data()

    file_name = f"{data_grouped[0]['login']}.txt"
    assert os.path.isfile(file_name)
    os.remove(file_name)
