from django.test import TestCase
from rest_framework.test import APITestCase, RequestsClient

# Create your tests here.
TEST_DATA = {'apartaments': 34000,
            'city': 'Рівне',
            'country': 'Україна',
            'house_num': 46,
            'street': 'Київська',
            'zip_code': 33027}

class API_Testing(APITestCase):
    def setUp(self):
        self.client = RequestsClient()
        self.client.post('http://127.0.0.1:8000/address/',
                        data=TEST_DATA)

    def test_post_address(self):
        TEST_DATA['appartaments'] = 100
        response = self.client.post('http://127.0.0.1:8000/address/',
                                    data=TEST_DATA)
        # print(response.json(), response.status_code)
        self.assertEqual(response.status_code, 201)

    def test_get_addreses(self):
        response = self.client.get('http://127.0.0.1:8000/address/')
        print(response.json(), response.status_code)
        self.assertEqual(response.status_code, 200)