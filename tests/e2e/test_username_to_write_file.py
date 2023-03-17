import json
from src.main import pursuit_profile
import os.path


def test_successfully_pursuit_profile(valid_username, valid_input_write_github_user_file):
    # Test that the function has expected behavior.
    pursuit_profile(valid_username)

    with open(f"{valid_username}.txt", 'r') as f:
        data_loaded = f.read()
        data_dicted = json.loads(data_loaded.replace("'", '"'))

        del valid_input_write_github_user_file['login']

        assert data_dicted == valid_input_write_github_user_file

    os.remove(f"{valid_username}.txt")
