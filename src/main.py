import logging

from requests import HTTPError
from src.use_cases.github_profile_processor import GitHubProfileProcessor

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
    except (KeyError, TypeError, IndexError, PermissionError, HTTPError):
        raise
