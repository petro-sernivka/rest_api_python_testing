import requests
import json


def test_post():
    r = requests.post('https://httpbin.org/post', data={'key': 'value'})
    print(r)
