import requests
import re

from rest_api_python_testing.consts import *

resp = requests.post(url=URL, data=PAYLOAD)
resp_body = resp.json()


# Positive tests
# POST request returns 200 status code
def test_post_status_code():
    assert resp.status_code == 200, \
        f'Response status code should be 200, not {resp.status_code}'
    assert resp.reason == 'OK', \
        f'"{resp.reason}" message returned instead of "OK"'


# Schema validation: fields name "status_code" (int type) and "hash_value" (str type)
def test_schema_validation():
    assert list(resp_body.keys()) == RESPONSE_SCHEMA_FIELDS, \
        f'Expected fields: {RESPONSE_SCHEMA_FIELDS}, actual fields: {list(resp_body.keys())}'
    assert isinstance(resp_body['status_code'], int), \
        f'"status_code" field should be "int" type, not "{type(resp_body["status_code"]).__name__}"'
    assert isinstance(resp_body['hash_value'], str), \
        f'"status_code" field should be "str" type, not "{type(resp_body["hash_value"]).__name__}"'


# "hash_value" matches a regular expression
def test_post_hash_value():
    assert re.match(pattern=HASH_VALUE_PATTERN, string=resp_body['hash_value']), \
        f'"hash_value" does not match a pattern: xxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx, ' \
        f'actual "hash_value": {resp_body["hash_value"]}'


# Verifying the data was saved correctly
def test_data_is_posted():
    assert resp_body['status_code'] == 0, \
        f'"status_code" should be 0, not {resp_body["status_code"]}'


# Verifying the same "hash_value" for multiple POST of the same email
def test_multiple_post():
    resp_1 = requests.post(url=URL, data=PAYLOAD)
    resp_body_1 = resp_1.json()
    resp_2 = requests.post(url=URL, data=PAYLOAD)
    resp_body_2 = resp_2.json()

    assert resp_body_1['hash_value'] == resp_body_2['hash_value'], \
        f'Multiple POST of the same email should return the same "hash_value"\n' \
        f'First "hash_value" for {PAYLOAD["email"]} is {resp_body_1["hash_value"]}\n' \
        f'Second "hash_value" for {PAYLOAD["email"]} is {resp_body_2["hash_value"]}\n'


# Verifying headers are as expected
def test_headers_list():
    for header in resp.headers._store:
        assert header in EXPECTED_HEADERS, \
            f'"{header}" header is not in expected headers list {EXPECTED_HEADERS}'


# Response time < 50 ms
def test_response_time():
    assert resp.elapsed.microseconds / 1000 < ACCEPTABLE_RESPONSE_TIME, \
        f'Expected response time: {ACCEPTABLE_RESPONSE_TIME} ms, ' \
        f'actual response time: {resp.elapsed.microseconds / 1000} ms'


# Negative tests
# Invalid value for email parameter
def test_invalid_email():
    for email in INVALID_EMAILS:
        resp_inv = requests.post(url=URL, data={'email': email})
        resp_body_inv = resp_inv.json()

        assert resp_inv.status_code == 400, \
            f'Response status code should be 400, not {resp_inv.status_code} for "{email}" email'

        assert resp_body_inv['status_code'] == 2, \
            f'"status_code" should be 2, not {resp_body_inv["status_code"]} for "{email}" email'

        assert resp_body_inv['message'] == INVALID_EMAIL_MESSAGE, \
            f'"message" should be {INVALID_EMAIL_MESSAGE}, not {resp_body_inv["message"]} for "{email}" email'


# Invalid values in HTTP headers
def test_invalid_header_value():
    resp_sess = requests.Session()
    resp_sess.headers.update(INVALID_HEADER_VALUE)
    resp_sess = resp_sess.post(url=URL, data=PAYLOAD)

    assert resp_sess.status_code == 400, \
        f'Response status code should be 400, not {resp_sess.status_code}'


# Unsupported methods for endpoints
def test_unsupported_methods():
    for method in UNSUPPORTED_METHODS:
        resp_unsupported = requests.request(method=method, url=URL, data=PAYLOAD)

        assert resp_unsupported.status_code == 404, \
            f'Response status code should be 404, not {resp_unsupported.status_code} for "{method}" method'


# Destructive tests
# Empty value for email parameter
def test_empty_email():
    resp_empty_email = requests.post(url=URL, data={'email': ''})
    resp_empty_email_json = resp_empty_email.json()

    assert resp_empty_email.status_code == 400, \
        f'Response status code should be 400, not {resp_empty_email.status_code} for empty email'

    assert resp_empty_email_json['status_code'] == 2, \
        f'"status_code" should be 2, not {resp_empty_email_json["status_code"]} for empty email'

    assert resp_empty_email_json['message'] == EMPTY_EMAIL_MESSAGE, \
        f'"message" should be {EMPTY_EMAIL_MESSAGE}, not {resp_empty_email_json["message"]} for empty email'


# Incorrect HTTP headers
