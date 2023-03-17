from typing import Dict, Tuple
import logging

from src.entities.user_github import DataSifted, GroupedUserData

logger = logging.getLogger(__name__)


# TODO: entitie de input
def data_sift(user_data: GroupedUserData) -> DataSifted:
    """
    This sift the raw user data to intended user data

    Args:
    -----
        - user_data (GroupedUserData): A tuple of user basic info and repositorie

    Return:
    -------
        - DataSifted: Sifted user data

    Example:
    --------
    """
    try:
        user_summary = {
            "login": user_data[0]["login"],
            "name": user_data[0]["name"],
            "url": user_data[0]["url"],
            "public_repositories": user_data[0]["public_repos"],
            "followers": user_data[0]["followers"],
            "following": user_data[0]["following"],
            "repositories_name_list": [
                repository["name"] for repository in user_data[1]
            ],
        }
    except (KeyError, IndexError, TypeError) as error:
        logger.exception(
            "failed_writing_data",
            extra={"error_message": str(error)},
        )
        raise

    return user_summary


# TODO: entitie de input
def write_github_user_file(github_user_data: DataSifted) -> None:
    """This dump the user data into a .txt file

    Args:
    -----
        github_user_data (DataSifted): Intended user data

    Return:
    -------
        - None: A .txt file will be created with user data in a dict structure

    Example:
    --------
    """
    try:
        file_name = f"{github_user_data['login']}.txt"
        del github_user_data['login']
        with open(file_name, "w") as _file:
            _file.write(str(github_user_data))
    except (KeyError, TypeError, PermissionError) as error:
        logger.exception(
            "failed_writing_data",
            extra={"error_message": str(error)},
        )
        raise
