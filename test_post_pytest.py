import requests
import json
import re
import psycopg2


url = 'http://localhost:3000/'
headers = {'Content-Type': 'application/json'}
payload = {'email': 'asd@asd.com'}

resp = requests.post(url=url, data=payload)
resp_body = resp.json()


# POST request returns 200 status code
def test_post_status_code():
    assert resp.status_code == 200


# Schema validation: fields name "status_code" (int type) and "hash_value" (str type)
def test_schema_validation():
    assert resp_body.keys() == ('status_code', 'hash_value')
    assert isinstance(resp_body['status_code'], int)
    assert isinstance(resp_body['hash_value'], str)


# "hash_value" matches a regular expression
def test_post_hash_value():
    assert re.match(pattern=r'[a-f0-9]{3}:[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}',
                    string=resp_body['hash_value'])


# Verifying the data was saved correctly (by SQL query)


# Verifying the same "hash_value" for multiple POST of the same email


# Verifying headers are as expected


# Response time < 50 ms
def test_response_time():
    assert resp.elapsed.microseconds / 1000 < 50
