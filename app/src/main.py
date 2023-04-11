import logging

from requests.exceptions import HTTPError

from src.entities.dump_data_processor import GitProfileDumperToFile
from src.entities.exceptions import GitHubApiRateLimitExceedeError
from src.entities.github_api_client import GitHubClient
from src.use_cases.exception import GitProfileDataDumperError
from src.use_cases.github_profile_processor import GitProfileProcessor

logger = logging.getLogger(__name__)


def extract_github_user_profile(user_name: str, access_token: str) -> None:
    """
    Extracts the profile data of a GitHub user using the GitProfileProcessor
    class and writes it to a file using the GitProfileDumperToFile class. It
    catches exceptions raised during the process and re-raises them.

    Args:
        - user_name (str):  The GitHub username for which the profile data
        needs to be extracted.

    Return: ->
        It either completes the process of extracting user profile data and
        writing it to a file or raises an exception.

    Raises:
        - HTTPError: Raised if an HTTP error occurs while communicating
        with the GitHub API.
        - GitHubApiRateLimitExceedeError: Raised if the GitHub API rate
        limit has been exceeded.
        - GitProfileDataDumperError :Raises when there is an error during
          the Git profile data dumping process.
    """

    github_client = GitHubClient()
    git_profile_dumper_to_file = GitProfileDumperToFile()
    git_profile_processor = GitProfileProcessor(
        user_name,  access_token, github_client, git_profile_dumper_to_file,
    )
    try:
        _execute_profile_extraction(git_profile_processor)

    except (
        HTTPError,
        GitHubApiRateLimitExceedeError,
        GitProfileDataDumperError,
    ):
        raise


def _execute_profile_extraction(
    git_profile_processor: GitProfileProcessor,
) -> None:
    """Executes the steps for extracting the user profile data and writing it
      to a file.

    Args:
        profile_processor (GitProfileProcessor): An instance of the
        GitProfileProcessor class.

    Raises:
        - HTTPError: Raised if an HTTP error occurs while communicating with
          the GitHub API.
        - GitHubApiRateLimitExceedeError: Raised if the GitHub API rate limit
          has been exceeded.
        - GitProfileDataDumperError :Raises when there is an error during
          the Git profile data dumping process.
    """

    try:
        git_profile_processor.group_user_data()
    except HTTPError as error:
        raise HTTPError(
            f"Failed to request user data from GitHub: {error}"
        ) from error
    except GitHubApiRateLimitExceedeError as error:
        raise GitHubApiRateLimitExceedeError(
            f"GitHub API rate limit exceeded: {error}"
        ) from error
    except GitProfileDataDumperError as error:
        raise GitProfileDataDumperError(
            f"Failed to data dumping/wrinting git profile data. {error}"
        ) from error
    logger.info("Request successful")

    logger.info("Writing data to file")
    try:
        git_profile_processor.dump_user_data()
    except Exception as error:
        raise Exception(  # pylint: disable=W0719
            f"Failed to write data to file: {error}"
        ) from error
    logger.info("Write successful")
