import logging
from locust import HttpLocust, TaskSet, task, events
from reporter import Reporter
from kc_config import *
from kc_task1 import *
from kc_task2 import *
from kc_task3 import *
from kc_task5 import *
from kc_task7 import *
from kc_task8 import *
from kc_task9 import *
from kc_task11 import *

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
                '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)

def login(l):
    l.client.post("/vektordata/authenticate/local", json=CONFIG['local'])
    l.client.get("/vektordata/authenticate/user")

class MainTask(TaskSet):
    tasks = {Task1 : 1, Task2 : 1, Task3 : 1, Task5 : 1, Task7 : 1, Task8 : 1, Task9 : 1, Task11 : 1}
    def on_start(self):
        login(self)

class WebsiteUser(HttpLocust):
    task_set = MainTask
    min_wait = 5000
    max_wait = 9000

"""
Here we trap some events
"""
reporter = Reporter()
events.request_success += reporter.request_success
events.hatch_complete += reporter.hatch_complete
