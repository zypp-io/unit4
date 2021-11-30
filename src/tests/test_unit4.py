import logging

from src.tests import unit4


def test_transactions():
    logging.info("start test transactions...")
    # unit4.run()
    logging.info("finished test transactions!")


def test_request_access_token():
    logging.info("requesting access token...")
    access_token = unit4.request_access_token()
    assert len(access_token) == 976
    logging.info("access token succesfully obtained!")


def test_list_administraties():
    logging.info("start test list administrations...")
    data = unit4.request_data(endpoint="/api/AdministrationGroupList/All")
    print(data)
    logging.info("test list administrations finished!")


if __name__ == "__main__":
    test_request_access_token()
    test_list_administraties()
