from django.test import TestCase
from rest_framework.test import APIClient

#from django.db import transaction

# For DRF, this decorator doesn't work, because DRF's APITestCase and APISimpleTestCase
# class uses atomic transaction for each of their methods.
# @transaction.atomic

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/products/'
    
    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        print("Test GET Passed.")

    def test_post_request(self):
        jacket = 'leather jacket'
        price = 599.99
        data = {
            'name': jacket,
            'description': 'This is is branded piece',
            'price': price
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], jacket)
        self.assertEqual(float(response.data['price']), price)
        print("Test POST Passed.")

    def test_put_request(self):
        # First create product
        jacket = 'leather jacket'
        data = {
            'name': jacket,
            'description': 'This is a branded jacket.',
            'price': 599.99
        }
        response = self.client.post(self.url, data)

        # Then update product
        primary_key = 1
        name = 'Leather Jacket'
        price = 999.99
        data = {
            'name': name,
            'description': 'Newly updated product.',
            'price': price
        }
        response = self.client.put(self.url + f"update/{primary_key}/", data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], name)
        self.assertEqual(float(response.data['price']), price)
        print("Test PUT Passed.")

    def test_delete_request(self):
        # First create product
        jacket = 'leather jacket'
        data = {
            'name': jacket,
            'description': 'This is a branded jacket.',
            'price': 599.99
        }
        response = self.client.post(self.url, data)

        # Then delete product
        primary_key = 1
        response = self.client.delete(self.url + f"delete/{primary_key}/")
        self.assertEqual(response.status_code, 204)
        print("Test DELETE Passed.")
