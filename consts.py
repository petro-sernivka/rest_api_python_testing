# POST request params
URL = 'http://localhost:3000/'
PAYLOAD = {'email': 'test@test.com'}

RESPONSE_SCHEMA_FIELDS = ['status_code', 'hash_value']

HASH_VALUE_PATTERN = r'[a-f0-9]{3}:[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'

EXPECTED_HEADERS = ('content-type', 'content-length', 'etag', 'date', 'connection', 'keep-alive')

ACCEPTABLE_RESPONSE_TIME = 50
