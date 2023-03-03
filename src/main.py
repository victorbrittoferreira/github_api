import logging

from requests import HTTPError
from src.use_cases.github_profile_processor import GitHubProfileProcessor
from config import GITHUB_USER_NAME

logger = logging.getLogger(__name__)


def pursuit_profile(user_name: str) -> None:
    profiled_user = GitHubProfileProcessor(user_name)
    try:
        logger.info("requesting_user_data_in_github")
        profiled_user.group_user_data()

        logger.info("successful_request")

        logger.info("wrinting_data_in_txt_file")
        profiled_user.dump_user_data()

        logger.info("successful_procedure_concluded")
    except (KeyError, IndexError, PermissionError, HTTPError):
        raise
