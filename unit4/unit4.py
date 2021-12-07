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

    def administrations(self) -> pd.DataFrame:
        """
        Function for extracting a table of available administrations
        Returns
        -------
        df: pd.DataFrame
            dataset containing administration names and values.
        """

        data = self.request_data(endpoint="api/AdministrationNVL")
        df = pd.DataFrame(data)

        return df

    def accounts(self, database: str, fiscal_year: int) -> pd.DataFrame:
        """
        Function for extracting account information.

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

    def account_categories(self, database: str) -> pd.DataFrame:
        """
        Function for getting account categories. Thesse categories entail the mapping of accounts in the trial balances
        and ultimately the annual reports.

        Parameters
        ----------
        database: str
            name of the administration.

        Returns
        -------
        df: pd.DataFrame
            dataset containing Account category names and values.
        """

        data = self.request_data(endpoint=f"api/{database}/AccountCategoryNVL")
        df = pd.DataFrame(data)
        df["administration"] = database

        return df

    def journals(self, database: str) -> pd.DataFrame:
        """
        Function for getting journal information.

        Parameters
        ----------
        database: str
            name of the administration.

        Returns
        -------
        df: pd.DataFrame
            journal information, including journal type.
        """

        data = self.request_data(endpoint=f"api/{database}/JournalInfoList")
        df = pd.DataFrame(data)
        df["administration"] = database
        df = df[["administration", "journalId", "journalType", "description"]].copy()
        df.rename(columns={"description": "journal_description"}, inplace=True)
        journal_types = self.journal_types(database)
        df = df.merge(journal_types, on=["administration", "journalType"], how="left", validate="m:1")

        return df

    def customers_suppliers(self, database: str) -> pd.DataFrame:
        """
        Function for getting Customer and Supplier information.

        Parameters
        ----------
        database: str
            name of the administration.

        Returns
        -------
        df: pd.DataFrame
            Customer & Supplier information.
        """
        df_list = []
        for relation_type in ["Customer", "Supplier"]:
            data = self.request_data(endpoint=f"api/{database}/{relation_type}InfoList")
            df = pd.DataFrame(data)
            df = df[[f"{relation_type.lower()}Id", "name"]].copy()
            df["administration"] = database
            df["relation_type"] = relation_type
            df.rename(columns={"name": "relation_name", f"{relation_type.lower()}Id": "relation_id"}, inplace=True)
            df_list.append(df)
        data = pd.concat(df_list, axis=0, sort=False, ignore_index=True)

        return data

    def journal_types(self, database: str) -> pd.DataFrame:
        """
        Function for getting journal information.

        Parameters
        ----------
        database: str
            name of the administration.
        Returns
        -------
        df: pd.DataFrame
            dataset containing journal_types
        """

        data = self.request_data(endpoint=f"api/{database}/JournalTypeNVL")
        df = pd.DataFrame(data)
        df["administration"] = database
        df.rename(columns={"name": "journalType", "value": "journaltype_description"}, inplace=True)
        df["journalType"] = df.journalType.astype(int)

        return df

    def costcenters(self, database: str) -> pd.DataFrame:
        """
        Function for getting journal information.

        Parameters
        ----------
        database: str
            name of the administration.
        Returns
        -------
        df: pd.DataFrame
            dataset containing journal_types
        """

        data = self.request_data(endpoint=f"api/{database}/CostCentreNVL")
        df = pd.DataFrame(data)
        df["administration"] = database
        df.rename(columns={"name": "costCentreId", "value": "costcenter_description"}, inplace=True)

        return df

    def transactions_by_year(self, database: str, fiscal_year: int) -> pd.DataFrame:
        """
        Function for pulling the transactions for a certain year.

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
        data = pd.DataFrame(
            self.request_data(endpoint=f"api/{database}/JournalEntryLineInfoList/ByPeriod/{fiscal_year}/0/12")
        )
        df = pd.DataFrame(data)
        df["administration"] = database

        return df

    def trial_balance(self, database: str, fiscal_year: int) -> pd.DataFrame:
        """
        Function for extracting trial balances.

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
