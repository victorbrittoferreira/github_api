import logging
import os
from dataclasses import asdict

from src.entities.Interfaces.git_profile_data_dumper_interface import (
    GitProfileDataDumperInterface,
)
from src.schemas.git_profile import FilteredData, GroupedUserData
from src.use_cases.exception import GitProfileDataDumperError

logger = logging.getLogger(__name__)


class GitProfileDumperToFile(GitProfileDataDumperInterface):
    """
    This class implements the GitProfileDataDumperInterface and dumps GitHub
      user data into a .txt file.

    Args:
        - user_raw_data (GroupedUserData, optional): A tuple of user basic
        info and repositories.

    Attributes:
        - user_raw_data (GroupedUserData): A tuple of user basic info and
        repositories.
        - _user_profile_data_extracted (dict): The user profile data that
          has been extracted and sifted.

    Methods:
        - extract_user_summary(self) -> FilteredData:
            Sifts the raw user data to intended user data.

        - dump_user_data(self) -> None:
            Dumps the user data into a .txt file.
    """

    __slots__ = ("user_raw_data", "_user_profile_data_extracted")

    def __init__(self, user_raw_data: GroupedUserData = None) -> None:
        self.user_raw_data: GroupedUserData = user_raw_data
        self._user_profile_data_extracted: FilteredData = None

    def extract_user_summary(self) -> FilteredData:
        """
        Sifts the raw user data to intended user data.

        Returns:
            FilteredData: Sifted user data.
        """
        try:
            user_summary = {
                "name": self.user_raw_data.user_data.user_basic_data["name"],
                "url": self.user_raw_data.user_data.user_basic_data["url"],
                "public_repositories": self.user_raw_data.user_data.user_basic_data[
                    "public_repos"
                ],
                "followers": self.user_raw_data.user_data.user_basic_data[
                    "followers"
                ],
                "following": self.user_raw_data.user_data.user_basic_data[
                    "following"
                ],
                "repositories_name_list": [
                    repository["name"]
                    for repository in self.user_raw_data.user_repositories.repositories
                ],
            }
            validaded_user_summary = FilteredData(user_summary)
            self._user_profile_data_extracted = validaded_user_summary

        except Exception as error:  # pylint: disable=W0718
            logger.exception(
                "failed_extracting_profile",
                extra={"error_message": str(error)},
            )

        return validaded_user_summary

    def dump_user_data(self) -> None:
        """
        Dumps the user data into a .txt file.

        Raises:
            GitProfileDataDumperError: If there is an error writing data.
            IOError: If there is an input/output error while writing data.

        Returns: -> None
            A .txt file will be created with user data in a dict structure.
        """
        try:
            profile_to_dump = self._user_profile_data_extracted
            user_name = (
                f"{profile_to_dump.data['name'].lower().replace(' ', '')}"
            )
            file_name = os.path.join("./", f"{user_name}.txt")

            with open(file_name, "w", encoding="utf-8") as _file:
                _file.write(str(asdict(profile_to_dump)))

        except OSError as error:
            logger.exception(
                "failed_writing_data",
                extra={"error_message": str(error)},
            )
            raise GitProfileDataDumperError(
                "Failed to data dumping/wrinting git profile data"
            ) from error
        except Exception as error:
            logger.exception(
                "failed_writing_data",
                extra={"error_message": str(error)},
            )
            raise

    def __str__(self) -> str:
        return f"""
        Git Profile Dumper To File:
            Client user_raw_data: {self.user_raw_data}
        """

    def __repr__(self) -> str:
        return f"GitProfileDumperToFile(user_raw_data={self.user_raw_data})"
