import logging
from typing import Tuple

from requests.exceptions import HTTPError

import src.services.dump_data_processor as services
from src.entities.github_api_client import GitHubClient
from src.entities.user_github import GroupedUserData

logger = logging.getLogger(__name__)


class GitHubProfileProcessor:
    """
        This class manages the data processing of a given profile in GitHub.
    The methods cat the user data and then dump it into a .txt file

    Attributes
    ----------
        - user_name: str
            User`s name

    Methods
    -------
        - group_user_data: Tuple

        - dump_user_data: None

    """

    __slots__ = ("user_name",)

    def __init__(self, user_name: str) -> None:
        self.user_name = user_name

    @property
    def user_data(self) -> None:
        return None

    def group_user_data(self) -> GroupedUserData:
        """
        This returns grouped user data, basic info and repositories

        Returns:
            - GroupedUserData: If the requestes were successful, this returns
            a tuple of basic profile info,like: name, url, public_repositories,
            followers, following.

        Example:
        --------
        >>> github_profile_processor = GitHubProfileProcessor(user_name)
        GitHubProfileProcessor(name=victorbrittoferreira, data=None)
        >>> github_profile_processor.group_user_data()
        (
            {'login': 'victorbrittoferreira', 'id': 34899711, 'node_id': ...},
            [[{'id': 486252178, 'node_id': 'R_kgDOHPuekg', 'name': ...]
        )



        """
        github_client = GitHubClient(self.user_name)
        try:
            repository_list = github_client.get_repositories_list()
            user_basic_profile_data = github_client.get_user_data()
        except HTTPError:
            raise

        GitHubProfileProcessor.user_data = (
            user_basic_profile_data,
            repository_list,
        )
        return user_basic_profile_data, repository_list

    def dump_user_data(self) -> None:
        """
        This returns grouped user data, basic info and repositories

        Return:
            - None: A .txt file will be created with user data in a dict structure

        Example:
        --------
        >>> github_profile_processor = GitHubProfileProcessor(user_name)
        GitHubProfileProcessor(name=victorbrittoferreira, data=None)
        >>> github_profile_processor.dump_user_data(
            {'login': 'victorbrittoferreira',  'url': 'https://api.github.com/users/vic..', ...},
            [{...}, {...}, {...}, {...}, {...}, ..]
        )

        """
        try:
            data_sifted = services.data_sift(self.user_data)
            services.write_github_user_file(data_sifted)
        except (KeyError, TypeError, IndexError, PermissionError):
            raise

    def __str__(self) -> str:
        return f"""
        GitHub Profile Processor:
            Profile name: {self.user_name}
            Profile data: {self.user_data}
        """

    def __repr__(self) -> str:
        return (
            f"GitHubProfileProcessor(name={self.user_name}, "
            f"data={self.user_data})"
        )
