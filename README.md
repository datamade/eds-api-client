# Electronic Disclosure Statement (EDS) API Client

```
# *Project title*

This driver allows other projects to interact with the City of Chicago's EDS system.

## Setup

### Dependencies

* [`lxml`](https://lxml.de/)
* [`scrapelib`](https://jamesturk.github.io/scrapelib/)

### Installation

`eds-api-client` is installable via pip.

## Usage
This driver provides three endpoints. In order to succesfully instantiate the `EDSAPIClient` class, provide values for `client_id`, `client_secret`, and `domain`. If no `domain` is provided, the default value is `https://apiqa.chicago.gov`

This driver provides three main functions:
1. Register a user

```
new_user_response = api_client.register_user(registration_data,
                                             app_username=client_username,
                                             app_password=client_password)
```

2. Log in a user
```
response = api_client._get_access_token(client_username, client_password)
```

3. Submit an EDS
```
response = api_client.submit_eds(submission_data, client_username, client_password)
```

## Copyright and attribution

Copyright (c) 2016 DataMade. Released under the [MIT License](https://github.com/datamade/your-repo-here/blob/master/LICENSE).
```