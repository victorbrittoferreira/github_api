import logging

from requests.exceptions import HTTPError
from src.main import dump_user_data, user_data_grouping


logger = logging.getLogger(__name__)


if __name__ == "__main__":
    # user_name = input("Insert the user name:\n")
    user_name = 'victorbrittoferreira'

    logger.info("requesting_user_data_in_github")
    user_data = user_data_grouping(user_name)

    logger.info("successful_request")

    logger.info("wrinting_data_in_txt_file")
    dump_user_data(user_data)

    logger.info("successful_procedure_concluded")
