import json
import os

import requests


class Unit4:
    def __init__(self):
        self.api_version = "V221"
        self.base_url = f"https://api.boekhoudgemak.nl/{self.api_version}"
        self.client_id = os.environ.get("UNIT4_CLIENT_ID")
        self.client_secret = os.environ.get("UNIT4_CLIENT_SECRET")
        self.refresh_token = os.environ.get("UNIT4_REFRESH_TOKEN")
        self.access_token = self.request_access_token()
        self.scope = ""

    def request_access_token(self):
        endpoint = "/Oauth/Token"
        url = self.base_url + endpoint
        response = requests.post(
            url,
            data={
                "refresh_token": self.refresh_token,
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "grant_type": "refresh_token",
            },
        )
        data = json.loads(response.text)
        access_token = data.get("access_token", "no access token")

        return access_token

    def request_data(self, endpoint: str):
        """

        Parameters
        ----------
        endpoint: str
            url endpoint (suffix) of the data that needs to be extracted

        Returns
        -------

        """
        url = self.base_url + endpoint
        response = requests.get(
            url, headers={"Accept": "application/json", "Authorization": f"Bearer {self.access_token}"}
        )

        data = json.loads(response.text)

        return data

    def run(self):
        pass
