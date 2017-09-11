from locust import HttpLocust, TaskSet, task
from kc_CONFIG import *
from kc_task1 import *
from kc_task2 import *
from kc_task3 import *
from kc_task5 import *
from kc_task7 import *
from kc_task8 import *
from kc_task9 import *
from kc_task11 import *

def login(l):
    l.client.post("/vektordata/authenticate/local", json=CONFIG['local'])
    l.client.get("/vektordata/authenticate/user")

class MainTask(TaskSet):
    tasks = {Task1 : 1, Task2 : 2, Task3 : 3, Task5 : 5, Task7 : 7, Task8 : 8, Task9 : 9, Task11 : 11}
    def on_start(self):
        login(self)

class WebsiteUser(HttpLocust):
    task_set = MainTask
    min_wait = 5000
    max_wait = 9000
