import requests
import json
import re


url = 'http://localhost:3000/'
headers = {'Content-Type': 'application/json'}
payload = {'email': '1@1.com'}

resp = requests.post(url=url, data=payload)


def test_post_status_code():
    assert resp.status_code == 200


def test_post_url():
    assert resp.url == url

    # assert resp_body['body']['status_code'] == 0
    # assert re.match(r'[a-f0-9]{3}:[a-f0-9]{32}', resp_body['body']['hash_value'])


def test_post_hash_value():
    assert re.match(r'[a-f0-9]{3}:[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}', resp.text)
