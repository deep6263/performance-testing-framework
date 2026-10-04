import os

from locust import HttpUser, between, task

from config.config import config
from utils.load_profile import get_profile


PROFILE_NAME = os.getenv("LOAD_PROFILE", "smoke")
PROFILE = get_profile(PROFILE_NAME)


class ApiUser(HttpUser):
    wait_time = between(1, 3)
    host = config.base_url

    @task
    def get_post(self):
        self.client.get("/posts/1", name="GET /posts/{id}")