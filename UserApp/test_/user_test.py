from unittest import TestCase
import requests


class Test_user(TestCase):
    def test_0_user_list(self):
        resp = requests.get('http://127.0.0.1:8000/user/list/')
        return resp.json()