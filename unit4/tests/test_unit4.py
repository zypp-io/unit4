import logging

from unit4.tests import unit4


def test_transactions():
    logging.info("start test transactions...")
    logging.info("finished test transactions!")


def test_request_access_token():
    logging.info("requesting access token...")
    unit4.request_access_token()
    logging.info("access token succesfully obtained!")


def test_list_administraties():
    logging.info("start test list administrations...")
    data = unit4.request_data(endpoint="api/AdministrationGroupList/All")
    print(data)
    logging.info("test list administrations finished!")


def test_fiscal_year_info():
    logging.info("start test fiscal year info...")
    administration = "MVL94315"
    fiscal_year = 2021
    data = unit4.request_data(endpoint=f"api/{administration}/FiscalYearInfo/{fiscal_year}")
    print(data)
    logging.info("test list fiscal year info finished!")


def test_customer_info_list():
    logging.info("start test customer info...")
    administration = "MVL94315"
    fiscal_year = 2021
    data = unit4.request_data(endpoint=f"api/{administration}/FiscalYearInfo/{fiscal_year}")
    print(data)
    logging.info("test list customer info finished!")


def test_accounts():
    logging.info("start test accounts to dataframe...")
    data = unit4.accounts(database="MVL94315", fiscal_year=2021)
    print(data.shape)
    logging.info("test accounts to dataframe finished!")


def test_account_info():
    logging.info("start test accounts to dataframe...")
    data = unit4.account_info(database="MVL94315", account_id="000900")
    print(data.shape)
    logging.info("test accounts to dataframe finished!")


if __name__ == "__main__":
    test_request_access_token()
    test_list_administraties()
    test_fiscal_year_info()
    test_accounts()
    test_account_info()
