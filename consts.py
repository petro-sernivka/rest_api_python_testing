# POST request params
URL = 'http://localhost:3000/'
PAYLOAD = {'email': 'test@test.com'}

RESPONSE_SCHEMA_FIELDS = ['status_code', 'hash_value']

HASH_VALUE_PATTERN = r'[a-f0-9]{3}:[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'

EXPECTED_HEADERS = ('content-type', 'content-length', 'etag', 'date', 'connection', 'keep-alive', 'x-powered-by',
                    'access-control-allow-origin')

ACCEPTABLE_RESPONSE_TIME = 50

INVALID_EMAILS = ('address',
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
                  'Abc..123@example.com')

INVALID_EMAIL_MESSAGE = 'Email is not valid'

INVALID_HEADER_VALUE = {'Content-Type': 'not_valid_value'}
