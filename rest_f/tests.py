from django.test import TestCase
from rest_framework.test import APITestCase, RequestsClient

# Create your tests here.
TEST_DATA = {'apartaments': 34,
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
        TEST_DATA['apartaments'] = 100
        response = self.client.post('http://127.0.0.1:8000/address/',
                                    data=TEST_DATA)
        self.assertEqual(response.status_code, 201)

    def test_get_addreses(self):
        response = self.client.get('http://127.0.0.1:8000/address/')
        self.assertEqual(response.status_code, 200)

    def test_get_address(self):
        response = self.client.get('http://127.0.0.1:8000/address/1/')
        self.assertEqual(response.status_code, 200)

    def test_get_address_incorrect_id(self):
        response = self.client.get('http://127.0.0.1:8000/address/20/')
        self.assertEqual(response.status_code, 404)

    def test_put_address(self):
        test_data = TEST_DATA.copy()
        test_data['apartaments'] = 200
        response = self.client.put('http://127.0.0.1:8000/address/1/',
                                    data=test_data)
        self.assertEqual(response.status_code, 200)

    def test_put_invalid_address(self):    
        test_data = TEST_DATA.copy()
        test_data['apartaments'] = 0
        response = self.client.put('http://127.0.0.1:8000/address/1/',
                                    data=test_data)
        print(response.json(), response.status_code)
        self.assertEqual(response.status_code, 400)
        self.assertIn('apartaments field cannot be less than zero',response.json()['non_field_errors'][0])


    def test_delete_address(self):    
        response = self.client.delete('http://127.0.0.1:8000/address/1/')
        self.assertEqual(response.status_code, 204)