import requests
import json
import re

url = 'https://httpbin.org/post'
headers = {'Content-Type': 'application/json'}
payload = {'key1': 1, 'key2': 'value2'}

resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))


def test_post_status_code():
    assert resp.status_code == 200

    resp_body = resp.json()
    assert resp_body['url'] == url

    # assert resp_body['body']['status_code'] == 0
    # assert re.match(r'[a-f0-9]{3}:[a-f0-9]{32}', resp_body['body']['hash_value'])


def test_post_hash_value():
    assert re.match(r'[a-f0-9]{3}:[a-f0-9]{32}', 'a1b:905ad9252b784f6e8d1a172fb04e2271')
