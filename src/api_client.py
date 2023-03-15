import scrapelib
import logging
import json


class AuthenticationError(Exception):
    pass


class EDSAPIClient(scrapelib.RetrySession):
    def __init__(self, client_id, client_secret, domain='https://apiqa.chicago.gov'):
        super().__init__()
        self._retry_attempts = 2
        self._retry_wait_seconds = 0.1
        self.domain = domain

        if not all([client_id, client_secret]):
            raise ValueError('Must provide a client_id and a client_secret.')
        else:
            self.client_id = client_id
            self.client_secret = client_secret

    def _get_access_token(self, username, password):
        """Returns a requests.response object with an access token."""

        url = "{domain}/edsapi/oauth/token".format(domain=self.domain)

        body = {
            'username': username,
            'password': password,
            'grant_type': 'password',
            'scope': 'write',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = self.post(url, data=body, headers=headers)

        if response.status_code == 200:
            return response
        else:
            logging.error('Failed to get access token for username: {username}'.format(username=username))
            raise AuthenticationError({'status_code': response.status_code,
                                       'content': str(response.content)})

    def submit_eds(self, eds_data, username, password):
        """Submits an EDS. Requires the EDS data and the vendor's username/password."""

        if not all([eds_data, username, password]):
            raise ValueError('Must provide eds_data, a username, and a password.')

        try:
            access_token_response = self._get_access_token(username=username, password=password)

            access_token = access_token_response.json()['access_token']

            headers = {
                'Authorization': "Bearer {token}".format(token=access_token),
                'Content-Type': 'application/json'
            }

            url = "{domain}/edsapi/rest/eds/".format(domain=self.domain)

            response = self.post(url, json=eds_data, headers=headers)
            return response
        except AuthenticationError as e:
            logging.error(e)

    def register_user(self, new_user_data, app_username, app_password):
        """Registers a new user. Requires the application's username and password."""

        if not all([new_user_data, app_username, app_password]):
            return ValueError('Must provide new_user_data, an app_username, and an app_password.')

        try:
            access_token_response = self._get_access_token(username=app_username, password=app_password)

            access_token = access_token_response.json()['access_token']

            headers = {
                'Authorization': "Bearer {token}".format(token=access_token),
                'Content-Type': 'application/json'
            }

            url = "{domain}/edsapi/rest/user/".format(domain=self.domain)
            response = self.post(url, json=new_user_data, headers=headers)
            return response
        except AuthenticationError as e:
            logging.error(e)

    def accept_response(self, response, **kwargs):
        """
        Sometimes, invalid requests will return a 500 or 400 response.
        A 500 might happen with invalid login credentials.
        """
        try:
            error_message = response.json().get('status', None)
        except json.decoder.JSONDecodeError:
            # occurs when the API returns an XML response
            error_message = None
        return (super().accept_response(response)
                or response.status_code == 500
                or 'Validation errors in your request' in error_message)
