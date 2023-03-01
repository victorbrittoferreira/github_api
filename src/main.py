from typing import Tuple
from src.entities.github_api_client import GitHubClient
from requests.exceptions import HTTPError
import logging
import src.services.dump_data_processor as services

logger = logging.getLogger(__name__)


def user_data_grouping(user_name: str) -> Tuple:
    github_client = GitHubClient(user_name)
    try:
        repository_list = github_client.get_repositories_list()
        user_basic_profile_data = github_client.get_user_data()
    except HTTPError as excepition:
        logger.error(
            "request_failed",
            extra={
                "response_error_message": str(excepition),
                "url": github_client.user_url,
            },
        )
        raise
    return user_basic_profile_data, repository_list


def dump_user_data(user_data) -> None:
    try:
        data_sifted = services.data_sift(user_data)
        services.write_github_user_file(data_sifted)
    except Exception as exception:
        logger.error(
            "failed_writing_data",
            extra={"error_message": str(exception)},
        )
        raise
