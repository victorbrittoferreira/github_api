import logging
from typing import Type

from requests import HTTPError

from src.entities.exceptions import GitHubApiRateLimitExceedeError
from src.entities.Interfaces.git_hosting_cloud_client_interface import (
    GitHostingCloudClientInterface,
)
from src.entities.Interfaces.git_profile_data_dumper_interface import (
    GitProfileDataDumperInterface,
)
from src.schemas.git_profile import GroupedUserData
from src.use_cases.exception import GitProfileDataDumperError

logger = logging.getLogger(__name__)


class GitProfileProcessor:

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

    __slots__ = (
        "user_name",
        "_git_hosting_service",
        "_git_profile_dumper",
        "_user_raw_data",
    )
    __slots__ = (
        "user_name",
        "_git_hosting_service",
        "_git_profile_dumper",
        "_user_raw_data",
        "access_token",
    )

    def __init__(
        self,
        user_name: str,
        access_token: str,
        git_hosting_service: Type[GitHostingCloudClientInterface],
        git_profile_dumper: Type[GitProfileDataDumperInterface],
    ) -> None:
        self.user_name = user_name
        self.access_token = access_token
        self._git_hosting_service = git_hosting_service
        self._git_profile_dumper = git_profile_dumper
        self._user_raw_data = None

        if not isinstance(git_hosting_service, GitHostingCloudClientInterface):
            raise TypeError(
                "The git_hosting_service attribute must be an instance of"
                " subclass GitHostingCloudClientInterface."
            )

        if not isinstance(git_profile_dumper, GitProfileDataDumperInterface):
            raise TypeError(
                "The git_profile_dumper attribute must be an"
                " instance of subclass GitProfileDataDumperInterface."
            )

    def group_user_data(self) -> GroupedUserData:
        """
        This returns grouped user data, basic info and repositories

        Returns:
            - GroupedUserData: If the requestes were successful, this returns
            a tuple of basic profile info,like: name, url, public_repositories,
            followers, following.

        Example:
        --------
        >>> github_profile_processor = GitProfileProcessor(user_name)
        GitProfileProcessor(name=victorbrittoferreira, data=None)
        >>> github_profile_processor.group_user_data()
        (
            {'login': 'victorbrittoferreira', 'id': 34899711, 'node_id': ...},
            [[{'id': 486252178, 'node_id': 'R_kgDOHPuekg', 'name': ...]
        )
        """
        try:
            self._git_hosting_service.user_name = self.user_name
            self._git_hosting_service.access_token = self.access_token
            user_repositories = (
                self._git_hosting_service.get_repositories_list()
            )
            user_basic_data = self._git_hosting_service.get_user_basic_data()

            user_raw_data = GroupedUserData(
                user_data=user_basic_data, user_repositories=user_repositories
            )
            self._user_raw_data = user_raw_data
        except (HTTPError, GitHubApiRateLimitExceedeError):
            raise
        except Exception as error:
            logger.exception(
                "failed_request_user_data",
                extra={"error_message": str(error)},
            )
            raise

        return user_basic_data

    def dump_user_data(self) -> None:
        """
        This returns grouped user data, basic info and repositories

        Return:
            - None: A .txt file will be created with user data in a dict structure

        Example:
        --------
        >>> github_profile_processor = GitProfileProcessor(user_name)
        GitProfileProcessor(name=victorbrittoferreira, data=None)
        >>> github_profile_processor.dump_user_data(
            {
                'login': 'victorbrittoferreira',
                'url': 'https://api.github.com/users/vic..',
            ...},
            [{...}, {...}, {...}, {...}, {...}, ..]
        )

        """
        try:
            self._git_profile_dumper.user_raw_data = self._user_raw_data
            self._git_profile_dumper.extract_user_summary()
            self._git_profile_dumper.dump_user_data()

        except GitProfileDataDumperError:
            raise

        except Exception as error:
            logger.exception(
                "failed_writing_user_data",
                extra={"error_message": str(error)},
            )
            raise

    def __str__(self) -> str:
        return f"""
        GitHub Profile Processor:
            Profile user_name: {self.user_name}
        """

    def __repr__(self) -> str:
        return f"GitProfileProcessor(user_name={self.user_name})"
