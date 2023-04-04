from abc import ABCMeta, abstractmethod


class GitHostingCloudClientInterface(metaclass=ABCMeta):
    """
    Interface for validating geometric objects.
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "request_user_profile_data")
            and callable(subclass.request_user_profile_data)
            and hasattr(subclass, "get_user_basic_data")
            and callable(subclass.get_user_basic_data)
            or NotImplemented
        )

    @abstractmethod
    def get_user_basic_data(self):
        """
        Validates if a given geometric object is within an acceptable geometric measurements

        Returns a string representation of the GitHostingCloudClientInterface.

        """
        raise NotImplementedError

    @abstractmethod
    def get_repositories_list(self):
        """
        Validates if a given geometric object is within an acceptable geometric measurements

        Returns a string representation of the GitHostingCloudClientInterface.

        """
        raise NotImplementedError
