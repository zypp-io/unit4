<p align="center">
  <img alt="logo" src="https://www.zypp.io/static/assets/img/logos/zypp/white/500px.png"  width="200"/>
</p>

Template repository for packages
===
> Package for pulling datasets using the Unit4 Multivers API


## Installation
```commandline
pip install unit4
```

## Usage
for an extensive list of examples, please refer to the [Unit4 test suite](unit4/tests/test_unit4.py).

```python
from unit4 import Unit4

unit4 = Unit4()
data = unit4.request_data(endpoint="/api/AdministrationGroupList/All")

```

## environment variables
The following environment variables need to be set:
- UNIT4_CLIENT_ID: the client id of the registered application
- UNIT4_CLIENT_SECRET: the client secret associated with the application
- UNIT4_REFRESH_TOKEN: The refresh token. To obtain the refresh token, please refer to the official [Unit 4 API Documentation](https://api.online.unit4.nl/V221/Documentation/Guide/OAuth)
