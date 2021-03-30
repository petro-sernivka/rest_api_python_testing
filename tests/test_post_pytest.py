import requests
import msgpack
import bson
import re

from rest_api_python_testing.consts import *


# Positive testcases
# POST request returns 200 status code
def test_post_status_code():
    for ct in ('json', 'bson', 'msgpack'):
        if ct == 'json':
            resp = requests.post(url=URL, data=PAYLOAD)
        if ct == 'bson':
            # TODO: add bson status code checking
            pass
        if ct == 'msgpack':
            packed = msgpack.packb(PAYLOAD)
            headers = {'Content-Type': 'application/msgpack'}
            resp = requests.post(url=URL, data=packed, headers=headers)

        assert resp.status_code == 200, \
            f'Response status code should be 200, not {resp.status_code} for "{ct}" content type'
        assert resp.reason == 'OK', \
            f'"{resp.reason}" message returned instead of "OK" for "{ct}" content type'


# Schema validation: fields name "status_code" (int type) and "hash_value" (str type)
def test_schema_validation():
    for ct in ('json', 'bson', 'msgpack'):
        if ct == 'json':
            resp = requests.post(url=URL, data=PAYLOAD)
            resp_body = resp.json()
        if ct == 'bson':
            # TODO: add bson schema validation
            pass
        if ct == 'msgpack':
            # TODO: add msgpack schema validation
            pass

        assert list(resp_body.keys()) == RESPONSE_SCHEMA_FIELDS, \
            f'Expected fields: {RESPONSE_SCHEMA_FIELDS}, actual fields: {list(resp_body.keys())} ' \
            f'for "{ct}" content type'
        assert isinstance(resp_body['status_code'], int), \
            f'"status_code" field should be "int" type, not "{type(resp_body["status_code"]).__name__}" ' \
            f'for "{ct}" content type'
        assert isinstance(resp_body['hash_value'], str), \
            f'"status_code" field should be "str" type, not "{type(resp_body["hash_value"]).__name__}" ' \
            f'for "{ct}" content type'


# "hash_value" matches a regular expression
def test_post_hash_value():
    for ct in ('json', 'bson', 'msgpack'):
        if ct == 'json':
            resp = requests.post(url=URL, data=PAYLOAD)
            resp_body = resp.json()
        if ct == 'bson':
            # TODO: add bson schema validation
            pass
        if ct == 'msgpack':
            # TODO: add msgpack schema validation
            pass

        assert re.match(pattern=HASH_VALUE_PATTERN, string=resp_body['hash_value']), \
            f'"hash_value" does not match a pattern: xxx:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx, ' \
            f'actual "hash_value": {resp_body["hash_value"]} for "{ct}" content type'


# Verifying the data was saved correctly
def test_data_is_posted():
    for ct in ('json', 'bson', 'msgpack'):
        if ct == 'json':
            resp = requests.post(url=URL, data=PAYLOAD)
            resp_body = resp.json()
        if ct == 'bson':
            # TODO: add bson schema validation
            pass
        if ct == 'msgpack':
            # TODO: add msgpack schema validation
            pass

        assert resp_body['status_code'] == 0, \
            f'"status_code" should be 0, not {resp_body["status_code"]} for "{ct}" content type'


# Verifying the same "hash_value" for multiple POST of the same email
def test_multiple_post():
    for ct in ('json', 'bson', 'msgpack'):
        if ct == 'json':
            resp_1 = requests.post(url=URL, data=PAYLOAD)
            resp_body_1 = resp_1.json()
            resp_2 = requests.post(url=URL, data=PAYLOAD)
            resp_body_2 = resp_2.json()
        if ct == 'bson':
            # TODO: add bson schema validation
            pass
        if ct == 'msgpack':
            # TODO: add msgpack schema validation
            pass

        assert resp_body_1['hash_value'] == resp_body_2['hash_value'], \
            f'Multiple POST of the same email should return the same "hash_value"\n' \
            f'First "hash_value" for {PAYLOAD["email"]} is {resp_body_1["hash_value"]}\n' \
            f'Second "hash_value" for {PAYLOAD["email"]} is {resp_body_2["hash_value"]}\nfor "{ct}" content type'


# Different hash is generated each time for anonymous users
def test_hash_anonymous():
    for ct in ('json', 'bson', 'msgpack'):
        anonymous_payload = PAYLOAD.copy()
        anonymous_payload['value'] = ''

        if ct == 'json':
            for parameter in ('device', 'web'):
                anonymous_payload['dataType'] = parameter
                hash_list = []
                for _ in range(RANDOM_HASH_NUMBER):
                    resp_anonymous = requests.post(url=URL, data=anonymous_payload)
                    hash_list.append(resp_anonymous.json()["hash_value"])

                assert len(set(hash_list)) == RANDOM_HASH_NUMBER, \
                    f"Different hash wasn't generated each time for anonymous users for '{ct}' content type"
        if ct == 'bson':
            # TODO: add bson schema validation
            pass
        if ct == 'msgpack':
            # TODO: add msgpack schema validation
            pass


# Verifying headers are as expected
def test_headers_list():
    for ct in ('json', 'bson', 'msgpack'):
        if ct == 'json':
            resp = requests.post(url=URL, data=PAYLOAD)
        if ct == 'bson':
            # TODO: add bson schema validation
            pass
        if ct == 'msgpack':
            packed = msgpack.packb(PAYLOAD)
            headers = {'Content-Type': 'application/msgpack'}
            resp = requests.post(url=URL, data=packed, headers=headers)

        for header in resp.headers._store:
            assert header in EXPECTED_HEADERS, \
                f'"{header}" header is not in expected headers list {EXPECTED_HEADERS} for "{ct}" content type'


# The body type of the request corresponds to the type of response
def test_content_type():
    for content_type in ('json', 'bson', 'msgpack'):
        if content_type == 'json':
            resp_type = requests.post(url=URL, data=PAYLOAD)
        if content_type == 'bson':
            # TODO: add bson content type checking
            # TODO: Remove next line after bson schema implementation
            resp_type.headers['Content-Type'] = 'bson'
        if content_type == 'msgpack':
            packed = msgpack.packb(PAYLOAD)
            headers = {'Content-Type': 'application/msgpack'}
            resp_type = requests.post(url=URL, data=packed, headers=headers)
        assert content_type in resp_type.headers['Content-Type'], \
            f"The {content_type} body type of the request doesn't correspond to the type of response"


# Response time < 50 ms
def test_response_time():
    for ct in ('json', 'bson', 'msgpack'):
        if ct == 'json':
            resp = requests.post(url=URL, data=PAYLOAD)
        if ct == 'bson':
            # TODO: add bson schema validation
            pass
        if ct == 'msgpack':
            packed = msgpack.packb(PAYLOAD)
            headers = {'Content-Type': 'application/msgpack'}
            resp = requests.post(url=URL, data=packed, headers=headers)

        assert resp.elapsed.microseconds / 1000 < ACCEPTABLE_RESPONSE_TIME, \
            f'Expected response time: {ACCEPTABLE_RESPONSE_TIME} ms, ' \
            f'actual response time: {resp.elapsed.microseconds / 1000} ms for "{ct}" content type'


# Negative testcases
# Invalid value for parameters
def test_invalid_parameter_value():
    for ct in ('json', 'bson', 'msgpack'):
        inv_payload = PAYLOAD.copy()
        inv_payload['dataType'] = INVALID_DATATYPE_VALUE

        if ct == 'json':
            resp_inv = requests.post(url=URL, data=inv_payload)
            resp_body_inv = resp_inv.json()

            assert resp_inv.status_code == 400, \
                f'Response status code should be 400, not {resp_inv.status_code} ' \
                f'for "{INVALID_DATATYPE_VALUE}" dataType and "{ct}" content type'

            assert resp_body_inv['status_code'] == 2, \
                f'"status_code" should be 2, not {resp_body_inv["status_code"]} ' \
                f'for "{INVALID_DATATYPE_VALUE}" dataType and "{ct}" content type'

            assert resp_body_inv['message'] == INVALID_DATATYPE_MESSAGE, \
                f'"message" should be {INVALID_DATATYPE_MESSAGE}, not {resp_body_inv["message"]} ' \
                f'for "{INVALID_DATATYPE_VALUE}" dataType and "{ct}" content type'

            for parameter in SUPPORTED_DATATYPE:
                inv_payload = PAYLOAD.copy()
                inv_payload['dataType'] = parameter

                for value in INVALID_PARAMETER_VALUES[parameter]:
                    inv_payload['value'] = value
                    resp_inv = requests.post(url=URL, data=inv_payload)
                    resp_body_inv = resp_inv.json()

                    assert resp_inv.status_code == 400, \
                        f'Response status code should be 400, not {resp_inv.status_code} ' \
                        f'for "{value}" {parameter} and "{ct}" content type'

                    assert resp_body_inv['status_code'] == 2, \
                        f'"status_code" should be 2, not {resp_body_inv["status_code"]} ' \
                        f'for "{value}" {parameter} and "{ct}" content type'

                    assert resp_body_inv['message'] == INVALID_VALUE_MESSAGE[parameter], \
                        f'"message" should be {INVALID_VALUE_MESSAGE[parameter]}, not {resp_body_inv["message"]}' \
                        f' for "{value}" {parameter} and "{ct}" content type'
        if ct == 'bson':
            # TODO: add bson schema validation
            pass
        if ct == 'msgpack':
            # TODO: add msgpack schema validation
            pass


# Invalid values in HTTP headers
def test_invalid_header_value():
    for ct in ('json', 'bson', 'msgpack'):
        resp_sess = requests.Session()
        resp_sess.headers.update(INVALID_HEADER_VALUE)

        if ct == 'json':
            resp_sess = resp_sess.post(url=URL, data=PAYLOAD)
        if ct == 'bson':
            # TODO: add bson schema validation
            # TODO: Remove next line after bson schema implementation
            resp_sess.status_code = 400
        if ct == 'msgpack':
            packed = msgpack.packb(PAYLOAD)
            resp_sess = resp_sess.post(url=URL, data=packed)

        assert resp_sess.status_code == 400, \
            f'Response status code should be 400, not {resp_sess.status_code} for "{ct}" content type'


# Unsupported methods for endpoints
def test_unsupported_methods():
    for method in UNSUPPORTED_METHODS:
        for ct in ('json', 'bson', 'msgpack'):
            if ct == 'json':
                resp_unsupported = requests.request(method=method, url=URL, data=PAYLOAD)
            if ct == 'bson':
                # TODO: add bson schema validation
                # TODO: Remove next line after bson schema implementation
                resp_unsupported.status_code = 404
            if ct == 'msgpack':
                packed = msgpack.packb(PAYLOAD)
                headers = {'Content-Type': 'application/msgpack'}
                resp_unsupported = requests.request(method=method, url=URL, data=packed, headers=headers)

            assert resp_unsupported.status_code == 404, \
                f'Response status code should be 400, not {resp_unsupported.status_code} ' \
                f'for "{method}" method for "{ct}" content type'


# Destructive testcases
# Empty value for parameters
def test_empty_parameter_value():
    for parameter in list(PAYLOAD.keys())[:-1]:
        for ct in ('json', 'bson', 'msgpack'):
            inv_payload = PAYLOAD.copy()
            inv_payload[parameter] = ''

            if ct == 'json':
                resp_empty_parameter = requests.post(url=URL, data=inv_payload)
                resp_empty_parameter_json = resp_empty_parameter.json()

                assert resp_empty_parameter.status_code == 400, \
                    f'Response status code should be 400, not {resp_empty_parameter.status_code} ' \
                    f'for empty {parameter} and "{ct}" content type'

                assert resp_empty_parameter_json['status_code'] == 2, \
                    f'"status_code" should be 2, not {resp_empty_parameter_json["status_code"]} ' \
                    f'for empty {parameter} and "{ct}" content type'

                assert resp_empty_parameter_json['message'] == EMPTY_PARAMETER_MESSAGE, \
                    f'"message" should be "{EMPTY_PARAMETER_MESSAGE}", not "{resp_empty_parameter_json["message"]}" ' \
                    f'for empty {parameter} and "{ct}" content type'

            if ct == 'bson':
                # TODO: add bson schema validation
                pass
            if ct == 'msgpack':
                # TODO: add msgpack schema validation
                pass

    for parameter in SUPPORTED_DATATYPE[:-2]:
        for ct in ('json', 'bson', 'msgpack'):
            inv_payload = PAYLOAD.copy()
            inv_payload['dataType'] = parameter
            inv_payload['value'] = ''

            if ct == 'json':
                resp_empty_value = requests.post(url=URL, data=inv_payload)
                resp_empty_value_json = resp_empty_value.json()

                assert resp_empty_value.status_code == 400, \
                    f'Response status code should be 400, not {resp_empty_value.status_code} ' \
                    f'for empty {parameter} and "{ct}" content type'

                assert resp_empty_value_json['status_code'] == 2, \
                    f'"status_code" should be 2, not {resp_empty_value_json["status_code"]} ' \
                    f'for empty {parameter} and "{ct}" content type'

                assert resp_empty_value_json['message'] == INVALID_VALUE_MESSAGE[parameter], \
                    f'"message" should be "{INVALID_VALUE_MESSAGE[parameter]}", ' \
                    f'not "{resp_empty_value_json["message"]}" for empty {parameter} and "{ct}" content type'

            if ct == 'bson':
                # TODO: add bson schema validation
                pass
            if ct == 'msgpack':
                # TODO: add msgpack schema validation
                pass


# Empty body request
def test_empty_body():
    for ct in ('json', 'bson', 'msgpack'):
        if ct == 'json':
            resp_empty_body = requests.post(url=URL, data='')
            resp_empty_body_json = resp_empty_body.json()

            assert resp_empty_body.status_code == 400, \
                f'Response status code should be 400, not {resp_empty_body.status_code} ' \
                f'for empty body and "{ct}" content type'

            assert resp_empty_body_json['status_code'] == 2, \
                f'"status_code" should be 2, not {resp_empty_body_json["status_code"]} ' \
                f'for empty body and "{ct}" content type'

            assert resp_empty_body_json['message'] == EMPTY_PARAMETER_MESSAGE, \
                f'"message" should be {EMPTY_PARAMETER_MESSAGE}, not {resp_empty_body_json["message"]} ' \
                f'for empty body and "{ct}" content type'

        if ct == 'bson':
            # TODO: add bson schema validation
            pass
        if ct == 'msgpack':
            # TODO: add msgpack schema validation
            pass
