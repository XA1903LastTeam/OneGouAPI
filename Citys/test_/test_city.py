#!/usr/bin/python3
# coding: utf-8

import requests
import unittest
from unittest import TestCase, TestSuite, TextTestRunner

import random


test_data = {

}

class City01TestCase(TestCase):

    def test_all_city(self):
        url = 'http://localhost:8000/city/all'
        resp = requests.get(url)
        city_list = resp.json().get('data')

        city = random.choice(city_list)

        test_data['city_id'] = city['id']
        print('---定位当前的城市--',
              city['city_name'],
              test_data['city_id'])


class City02TestCase(TestCase):
    def test_city_area(self):
        url = 'http://localhost:8000/city/area/'
        resp = requests.get(url, {
            'one_id': test_data['city_id']
        })

        area_list = resp.json().get('data')

        area = random.choice(area_list)

        print('---定位的区县--', area['cityareaname'])

        test_data['area_id'] = area['id']


def suite1():
    suite = TestSuite()
    suite.addTest(City01TestCase.test_all_city)
    return suite

def suite2():
    suite = TestSuite()
    suite.addTest(City02TestCase.test_city_area)

    return suite


def suite_all():
    return TestSuite((suite1(),
                      suite2()))

if __name__ == '__main__':
    TextTestRunner().run(suite_all())

