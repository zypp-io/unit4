import pandas as pd

from unit4.core import Base


class Unit4(Base):
    """
    Class for importing datasets using the Unit 4 API. For a full list of modules check the unit 4 documentation:
    https://api.multivers.nl/V221/Help. The request_data function returns a json object for the module and in the
    functions in this class the datasets are transformed into dataframes.
    """

    def __init__(self):
        super().__init__()

    def accounts(self, database: str, fiscal_year: int) -> pd.DataFrame:
        """

        Parameters
        ----------
        database: str
            name of the administration.
        fiscal_year: int
            fiscal year for request.

        Returns
        -------
        df: pd.DataFrame
            dataset containing account names and values.
        """

        data = self.request_data(endpoint=f"api/{database}/AccountNVL/All/{fiscal_year}")
        df = pd.DataFrame(data)
        df["administration"] = database
        df["fiscal_year"] = str(fiscal_year)

        return df

    def trial_balance(self, database: str, fiscal_year: int) -> pd.DataFrame:
        """

        Parameters
        ----------
        database: str
            name of the administration.
        fiscal_year: int
            fiscal year for request.

        Returns
        -------
        df: pd.DataFrame
            dataset containing account names and values.
        """

        data = self.request_data(endpoint=f"api/{database}/AccountPeriodTotalInfoList/{fiscal_year}")
        df = pd.DataFrame(data)
        df["administration"] = database
        df["fiscal_year"] = str(fiscal_year)

        return df

    def account_info(self, database: str, account_id: str):
        """
        Function for getting account information. In this information is the account category, which is relevant for
        getting the appropriate label in reports.

        Parameters
        ----------
        database: str
            name of the administration.
        account_id: str
            account id for request.

        Returns
        -------

        """

        data = self.request_data(endpoint=f"api/{database}/AccountInfo/{account_id}")
        df = pd.DataFrame(data, index=[0])
        df["administration"] = database

        return df

    def account_categories(self, database: str):
        """
        Function for getting account categories. Thesse categories entail the mapping of accounts in the trial balances
        and ultimately the annual reports.

        Returns
        -------
        df: pd.DataFrame
            dataset containing Account category names and values.
        """

        data = pd.DataFrame(self.request_data(endpoint=f"api/{database}/AccountCategoryNVL"))
        df = pd.DataFrame(data)
        df["administration"] = database

        return df

    def administrations(self) -> pd.DataFrame:
        """

        Returns
        -------
        df: pd.DataFrame
            dataset containing administration names and values.
        """

        data = self.request_data(endpoint="api/AdministrationNVL")
        df = pd.DataFrame(data)

        return df
