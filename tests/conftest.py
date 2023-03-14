import json
import pytest
# TODO: implement functionality that uses these imports
# from app import app
from tests.configs import settings as env # replace with env vars
from tests.dummy_data import SESSION_DATA
from tests.utils import unique_applicant
from eds_api_client.api_client import EDSAPIClient
from eds_api_client.web_client import EDSWebClient

@pytest.fixture
def app_creds():
    return {
        'client_id': env.EDS_CLIENT_ID,
        'client_secret': env.EDS_CLIENT_SECRET,
        'eds_domain': env.EDS_DOMAIN_NAME,
        'username': env.EDS_CLIENT_USERNAME,
        'password': env.EDS_CLIENT_PASSWORD
    }

@pytest.fixture
def api_client(app_creds):
    return EDSAPIClient(client_id=app_creds['client_id'],
                        client_secret=app_creds['client_secret'],
                        domain=app_creds['eds_domain'])

@pytest.fixture
def web_client():
    return EDSWebClient(env.TEST_VENDOR_USERNAME, env.TEST_VENDOR_PASSWORD)

@pytest.fixture
def user():
    username = env.TEST_VENDOR_USERNAME
    password = env.TEST_VENDOR_PASSWORD
    return username, password

@pytest.fixture
def valid_submission():
    with open('tests/fixtures/submission_valid.json') as f:
        valid_submission = json.load(f)
    return valid_submission

@pytest.fixture
def invalid_submission():
    with open('tests/fixtures/submission_invalid.json') as f:
        invalid_submission = json.load(f)
    return invalid_submission

@pytest.fixture
def new_user():
    with open('tests/fixtures/new_user_valid.json') as f:
        new_user = json.load(f)
    
    applicant = unique_applicant()
    new_user['user'].update({
        'userId': applicant[0],
        'email': applicant[1]
    })
    
    new_user['company'].update({
        'ssn': applicant[2]
    })
    return new_user

@pytest.fixture
def invalid_user():
    with open('tests/fixtures/new_user_invalid.json') as f:
        invalid_user = json.load(f)
    return invalid_user

