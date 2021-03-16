from locust import HttpUser, task, between
from rest_api_python_testing.consts import *
from datetime import datetime
from locust.env import Environment
from locust.stats import stats_printer, stats_history
from locust.log import setup_logging


class User(HttpUser):
    wait_time = between(1, 1.1)

    # @task
    def post_api_random(self):
        self.client.post(url=URL, data={'email': f'{str(datetime.now())[17:]}@1.com'})

    @task
    def post_api_existed(self):
        self.client.post(url=URL, data=PAYLOAD)


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
