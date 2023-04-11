import logging

import requests
from requests.exceptions import HTTPError

from src.entities.exceptions import GitHubApiRateLimitExceedeError
from src.entities.Interfaces.git_hosting_cloud_client_interface import (
    GitHostingCloudClientInterface,
)
from src.schemas.git_profile import UserBasicData, UserRepositories

logger = logging.getLogger(__name__)


class GitHubClient(GitHostingCloudClientInterface):

    """
    A class that uses the requests library to access data from a user on GitHub.
    This class has methods to retrieve basic data and a list of repositories
    from the user.


    Args:
    user_name : str
        The username of the GitHub user.

        - user_name: str
            User`s name

    Attributes:
    _user_basic_data(UserBasicData): A dict of user basic info
    _user_repositories(UserRepositories): A list of user repositories.
    Methods:
    - get_user_basic_data() -> UserBasicData:
        Returns the user's basic personal profile info.

    - get_repositories_list() -> UserRepositories:
        Returns the user's repositories list.

    Raises:
    - HTTPError:
        If an HTTP error occurs on the server or client side.

    - GitHubApiRateLimitExceedeError:
        If the rate limit of the GitHub API has been exceeded.

    Example
    >>> github_client = GitHubClient('victorbrittoferreira')
    >>> github_client.get_user_basic_data()
    {'login': 'victorbrittoferreira', 'id': 34899711,
     'node_id': 'MDQ6VXNlcjM0ODk5NzEx', ...}
    >>> github_client.get_repositories_list()
    [{'id': 486252178, 'node_id': 'R_kgDOHPuekg', 'name': 'angular_todo_list',
      'full_name': 'victorbrittoferreira..._todo_list', ...}]
    """

    __slots__ = ("user_name",)

    _BASE_URL = "https://api.github.com/users"

    def __init__(self, user_name: str = None, access_token: str = None) -> None:
        self.user_name = user_name
        self.access_token = access_token
        self._user_basic_data = None
        self._user_repositories = None

    @property
    def user_url(self) -> str:
        """
        Returns the URL of the GitHub user profile.
        """
        return f"{self._BASE_URL}/{self.user_name}"

    @staticmethod
    def _request_user_profile_data(
        url: str,
        access_token
    ) -> UserRepositories | UserBasicData:
        """
        Sends an HTTP GET request to the specified URL and returns the response
        as a dictionary of user profile data.

        Parameters
        ----------
        url : str
            The URL to send the GET request to.

        Returns
        -------
        Union[UserRepositories, UserBasicData]:
            A dictionary of user profile data.

        Raises
        ------
        HTTPError:
            If an HTTP error occurs on the server or client side.

        GitHubApiRateLimitExceedeError:
            If the rate limit of the GitHub API has been exceeded.
        """
        attempts = 3
        for attempt in range(1, attempts):
            try:
                headers = {
                    "Authorization": f"Bearer {access_token}"
                }

                response = requests.get(url, headers=headers, timeout=15)
                if response.status_code == 200:
                    raw_data = response.json()
                    break

                if (
                    response.status_code == 403
                    and "rate limit exceeded" in response.text  # noqa: W503
                ):
                    raise GitHubApiRateLimitExceedeError(
                        "GitHub API rate limit exceeded"
                    )

                if attempt == attempts:
                    logger.debug("requesting_user_data_in_hosting_cloud_fail")
                    response.raise_for_status()

            except (HTTPError, GitHubApiRateLimitExceedeError) as error:
                logger.exception(
                    "request_failed",
                    extra={
                        "response_error_message": str(error),
                        "url": url,
                    },
                )
                raise
        return raw_data

    def get_user_basic_data(self) -> UserBasicData:
        """
        Retrieves the user's basic personal profile info from the GitHub API.

        Returns
        -------
        UserBasicData:
            A dictionary containing the user's basic personal profile info.

        Raises:
        ------
            - HTTPError:
                Raises when an HTTP error occur in the server or client side.

        Example:
        --------
            >>> github_client = GitHubClient('victorbrittoferreira')
            >>> github_client.get_user_basic_data()
            {login': 'victorbrittoferreira', 'id': 34899711,
             'node_id': 'MDQ6VXNlcjM0ODk5NzEx', ...}
        """
        try:
            user_basic_raw_data = self._request_user_profile_data(
                self.user_url, self.access_token
            )
            validated_user_basic_raw_data = UserBasicData(user_basic_raw_data)
            self._user_basic_data = validated_user_basic_raw_data
        except (HTTPError, GitHubApiRateLimitExceedeError):
            raise

        return validated_user_basic_raw_data

    def get_repositories_list(self) -> UserRepositories:
        """
        Retrieves the user's repositories profile info from the GitHub API.

        Returns:
        --------
            - UserRepositories:
            A list containing the user's repositories info.

        Example:
        --------
            >>> github_client = GitHubClient('victorbrittoferreira')
            >>> github_client.get_repositories_list()
            [{'id': 486252178, 'node_id': 'R_kgDOHPuekg', 'name': 'angular_todo_list',
              'full_name': 'victorbrittoferreira..._todo_list', ...}]

        Raises:
        ------
            - HTTPError:
                Raises when an HTTP error occur in the server or client side.
        """
        url = f"{self._BASE_URL}/{self.user_name}/repos"
        try:
            user_repositories_raw_data = self._request_user_profile_data(
                url, self.access_token)
            valited_user_repositories_raw_data = UserRepositories(
                user_repositories_raw_data
            )
            self._user_repositories = valited_user_repositories_raw_data
        except (HTTPError, GitHubApiRateLimitExceedeError):
            raise

        return valited_user_repositories_raw_data

    def __str__(self) -> str:
        return f"""
        GitHub Client:
            Client user_name: {self.user_name}
        """

    def __repr__(self) -> str:
        return f"GitHubClient(user_name={self.user_name})"
