from io import StringIO
from lxml import etree
import scrapelib


class EDSWebClient(scrapelib.RetrySession):
    """
    Web scraper for the EDS UI.
    """

    def __init__(
        self,
        username,
        password,
        domain="https://webapps1qa.chicago.gov/eds",
        retry_attempts=2,
    ):
        super(EDSWebClient, self).__init__()
        self._retry_attempts = retry_attempts
        self._retry_wait_seconds = 0.1

        if not username or not password:
            raise ValueError("Must provide a username and a password.")
        else:
            self.username = username
            self.password = password
            self.domain = domain

    def _login_user(self):
        """
        Returns a dict with the outcome of a user login.
        """
        login_url = "{domain}/login".format(domain=self.domain)

        # get the login page so we can get the CSRF token
        response = self.get(login_url)

        # parse out the CSRF token
        parser = etree.HTMLParser()
        html = response.content.decode("utf-8")
        tree = etree.parse(StringIO(html), parser)
        input_elements = tree.xpath("//input")

        csrf_token = [
            elem.get("value") for elem in input_elements if elem.get("name") == "_csrf"
        ]

        payload = {
            "_csrf": csrf_token[0],
            "username": self.username,
            "password": self.password,
        }

        login_response = self.post(login_url, data=payload)

        # determine login response since either valid or invalid credentials return a 200
        if b"Invalid User ID/Password combination" in login_response.content:
            login_response.status_code = 401
        elif "home" not in login_response.url:
            login_response.status_code = 500

        return login_response

    def get_eds_pdf(self, eds_id):
        """
        Returns an EDS PDF.
        """
        if not eds_id:
            raise ValueError("Must provide an EDS ID.")
        else:
            login_response = self._login_user()

            if login_response.status_code == 200:
                eds_pdf_url = "{domain}/pdf/single/{eds_id}".format(
                    domain=self.domain, eds_id=eds_id
                )
                response = self.get(eds_pdf_url)

                return response
            else:
                return login_response
