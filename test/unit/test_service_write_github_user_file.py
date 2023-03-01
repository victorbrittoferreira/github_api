import src.services as services
import os.path
import json


def test_created_file(valid_input_write_github_user_file):
    services.write_github_user_file(valid_input_write_github_user_file)

    file_name = valid_input_write_github_user_file['name'].replace(
        ' ', '_').lower()+'.txt'
    assert os.path.isfile(file_name)
    os.remove(file_name)


def test_correct_data_writed(valid_input_write_github_user_file):
    services.write_github_user_file(valid_input_write_github_user_file)

    file_name = valid_input_write_github_user_file['name'].replace(
        ' ', '_').lower()+'.txt'

    with open(file_name, 'r') as f:
        data_loaded = f.read()
        data_dicted = json.loads(data_loaded.replace("'", '"'))
        assert data_dicted == valid_input_write_github_user_file
    os.remove(file_name)
