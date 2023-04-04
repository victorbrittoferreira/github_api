from abc import ABCMeta, abstractmethod


class GitProfileDataDumperInterface(metaclass=ABCMeta):
    """
    Interface for validating geometric objects.
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "dump_user_data")
            and callable(subclass.dump_user_data)
            and hasattr(subclass, "extract_user_summary")
            and callable(subclass.extract_user_summary)
            or NotImplemented
        )

    @abstractmethod
    def extract_user_summary(self):
        """
        Validates if a given geometric object is within an acceptable geometric measurements

        Returns a string representation of the GitProfileDataDumperInterface.

        """
        raise NotImplementedError

    @abstractmethod
    def dump_user_data(self):
        """
        Validates if a given geometric object is within an acceptable geometric measurements

        Returns a string representation of the GitProfileDataDumperInterface.

        """
        raise NotImplementedError
