import requests
import json
import re
import psycopg2

from consts import *


resp = requests.post(url=URL, data=PAYLOAD)
resp_body = resp.json()


# POST request returns 200 status code
def test_post_status_code():
    assert resp.status_code == 200


# Schema validation: fields name "status_code" (int type) and "hash_value" (str type)
def test_schema_validation():
    assert list(resp_body.keys()) == RESPONSE_SCHEMA_FIELDS
    assert isinstance(resp_body['status_code'], int)
    assert isinstance(resp_body['hash_value'], str)


# "hash_value" matches a regular expression
def test_post_hash_value():
    assert re.match(pattern=HASH_VALUE_PATTERN, string=resp_body['hash_value'])


# Verifying the data was saved correctly (by SQL query)


# Verifying the same "hash_value" for multiple POST of the same email
def test_multiple_post():
    resp_1 = requests.post(url=URL, data=PAYLOAD)
    resp_body_1 = resp_1.json()
    resp_2 = requests.post(url=URL, data=PAYLOAD)
    resp_body_2 = resp_2.json()

    assert resp_body_1['hash_value'] == resp_body_2['hash_value']


# Verifying headers are as expected
def test_headers_list():
    for header in resp.headers._store:
        assert header in EXPECTED_HEADERS


# Response time < 50 ms
def test_response_time():
    assert resp.elapsed.microseconds / 1000 < ACCEPTABLE_RESPONSE_TIME
