from pytz import timezone
import pytest
import vcr

from datetime import datetime

from src.api_client import AuthenticationError, EDSAPIClient
from src.web_client import EDSWebClient


APP_TIMEZONE = timezone("America/Chicago")

MAINTENANCE_START = datetime(2019, 2, 6, 19, tzinfo=APP_TIMEZONE)
MAINTENANCE_END = datetime(2019, 2, 7, tzinfo=APP_TIMEZONE)


@vcr.use_cassette("tests/fixtures/vcr_cassettes/login_valid.yaml")
def test_valid_login(api_client, user):
    username, password = user

    response = api_client._get_access_token(username, password)

    assert response.status_code == 200


@vcr.use_cassette("tests/fixtures/vcr_cassettes/login_invalid.yaml")
def test_invalid_login(api_client):
    with pytest.raises(AuthenticationError):
        response = api_client._get_access_token("adalovelace", "password")


@vcr.use_cassette("tests/fixtures/vcr_cassettes/submission_valid.yaml")
def test_eds_submission(api_client, user, valid_submission):
    username, password = user

    response = api_client.submit_eds(valid_submission, username, password)

    assert response.status_code == 201


@vcr.use_cassette("tests/fixtures/vcr_cassettes/submission_invalid.yaml")
def test_invalid_eds_submission(api_client, user, invalid_submission):
    username, password = user

    response = api_client.submit_eds(invalid_submission, username, password)

    assert response.status_code == 400
    assert b"errors" in response.content
    assert b"BAD_REQUEST" in response.content


@vcr.use_cassette("tests/fixtures/vcr_cassettes/register_user.yaml")
def test_register_user(api_client, app_creds, new_user):
    response = api_client.register_user(
        new_user, app_creds["username"], app_creds["password"]
    )

    assert response.status_code == 200


@vcr.use_cassette("tests/fixtures/vcr_cassettes/register_user_invalid.yaml")
def test_invalid_register_user(api_client, app_creds, invalid_user):
    response = api_client.register_user(
        invalid_user, app_creds["username"], app_creds["password"]
    )
    assert response.status_code == 400


@vcr.use_cassette("tests/fixtures/vcr_cassettes/download_pdf_valid.yaml")
def test_download_pdf(web_client):
    eds_id = 23785
    pdf_response = web_client.get_eds_pdf(eds_id)
    assert pdf_response.status_code == 200


@vcr.use_cassette("tests/fixtures/vcr_cassettes/download_pdf_invalid.yaml")
def test_download_pdf_error(web_client):
    response = web_client.get_eds_pdf(20001)
    assert response.status_code == 403


def test_client_errors(api_client, web_client):
    with pytest.raises(TypeError):
        EDSAPIClient()

    with pytest.raises(TypeError):
        EDSWebClient()

    with pytest.raises(ValueError):
        EDSAPIClient("", "")

    with pytest.raises(ValueError):
        api_client.submit_eds({"data": [{"key": "value"}]}, "username", "")

    with pytest.raises(ValueError):
        api_client.submit_eds({}, "username", "password")

    with pytest.raises(TypeError):
        api_client.register_user("username", "password")

    with pytest.raises(TypeError):
        web_client.get_eds_pdf()
