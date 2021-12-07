<p align="center">
  <img alt="logo" src="https://www.zypp.io/static/assets/img/logos/zypp/white/500px.png"  width="200"/>
</p>

Unit4 Multivers API
===
> Package for pulling datasets using the Unit4 Multivers API

[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI](https://img.shields.io/pypi/v/unit4)](https://pypi.org/project/unit4/)
[![Latest release](https://badgen.net/github/release/zypp-io/unit4)](https://github.com/zypp-io/unit4/releases)


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
