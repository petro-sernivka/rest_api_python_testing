import pytest
import psycopg2
import requests


@pytest.fixture
def setup_database():
    def connect():
        conn = psycopg2.connect(
            host="localhost",
            database="uuid",
            user="postgres",
            password="postgres")

        cur = conn.cursor()
        return cur

    yield connect

    # cur.close()
    # conn.close()
