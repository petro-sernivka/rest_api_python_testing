import pytest
import requests
from utils.models import user as user_model

# from config import endpoints


# @pytest.fixture
# def user():
#     user_body = user_model()
#     response = requests.post(url=endpoints.USERS, data=user_body)
#     return user_body, response.json()['id']
