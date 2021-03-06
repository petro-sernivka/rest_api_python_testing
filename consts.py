import socket

# POST request params
URL = f'http://{socket.gethostbyname(socket.gethostname())}:3000/'
PAYLOAD = {"auth": "test",
           "sourceId": "123",
           "dataType": "email",
           "value": "test@test.com"}

SUPPORTED_DATATYPE = ('email', 'phone', 'device', 'web')

RESPONSE_SCHEMA_FIELDS = ['status_code', 'hash_value']

HASH_VALUE_PATTERN = r'[a-f0-9]{3}:[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'

EXPECTED_HEADERS = ('content-type', 'content-length', 'etag', 'date', 'connection', 'keep-alive', 'x-powered-by',
                    'access-control-allow-origin', 'server', 'vary')

ACCEPTABLE_RESPONSE_TIME = 50

RANDOM_HASH_NUMBER = 10

INVALID_PARAMETER_VALUES = {'email': ('address',
                                      '#@%^%#$@#$@#.com',
                                      '@example.com',
                                      'Joe Smith <email@example.com>',
                                      'email.example.com',
                                      'email@example@example.com',
                                      '.email@example.com',
                                      'email.@example.com',
                                      'email..email@example.com',
                                      'あいうえお@example.com',
                                      'email@example.com (Joe Smith)',
                                      'email@example',
                                      'email@-example.com',
                                      'email@111.222.333.44444',
                                      'email@example..com',
                                      'Abc..123@example.com'),
                            'phone': ('12345678901',
                                      '+1234567890a',
                                      '2345678901',
                                      '+abcdefghijk'),
                            'device': (),
                            'web': ()}

INVALID_DATATYPE_MESSAGE = 'Wrong dataType'
INVALID_VALUE_MESSAGE = {'email': 'value is not valid',
                         'phone': 'value is not valid',
                         'device': '',
                         'web': ''}
EMPTY_PARAMETER_MESSAGE = 'auth, sourceId, dataType and value parameters are required to make this request'

INVALID_DATATYPE_VALUE = 'invalid_datatype'
INVALID_HEADER_VALUE = {'Content-Type': 'not_valid_value'}

UNSUPPORTED_METHODS = ('HEAD', 'GET', 'PUT', 'PATCH', 'DELETE')
