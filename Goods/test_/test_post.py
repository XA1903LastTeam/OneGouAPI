from unittest import TestCase

import requests


class TestPost(TestCase):
    def test_post(self):
        url = 'http://localhost:8000/goods/gethome/'
        resp = requests.post(url)
        # self.assertEqual(resp.status_code, 200, '请求失败')

        print(resp)
        print(resp.text)
