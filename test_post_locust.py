import requests
import gevent
import pytest
import json

from locust import HttpUser, task, between
from locust.env import Environment
from locust.stats import stats_printer, stats_history
from locust.log import setup_logging


def test_post():
    response = requests.post('https://httpbin.org/post', data={'key': 'value'})
    assert response.status_code == 200


setup_logging("INFO", None)


class User(HttpUser):
    wait_time = between(0.1, 1)

    @task
    def hello_world(self):
        self.client.post('https://httpbin.org/post', data={'key1': 'value1'})

    # def on_start(self):
    #     self.client.post('https://httpbin.org/post', data={'key3': 'value3'})


# # setup Environment and Runner
# env = Environment(user_classes=[User])
# env.create_local_runner()
#
# # start a WebUI instance
# env.create_web_ui("127.0.0.1", 8089)
#
# # start a greenlet that periodically outputs the current stats
# gevent.spawn(stats_printer(env.stats))
#
# # start a greenlet that save current stats to history
# gevent.spawn(stats_history, env.runner)
#
# # start the test
# env.runner.start(1, spawn_rate=3)
#
# # in 60 seconds stop the runner
# gevent.spawn_later(10, lambda: env.runner.quit())
#
# # wait for the greenlets
# env.runner.greenlet.join()
#
# # stop the web server for good measures
# env.web_ui.stop()
