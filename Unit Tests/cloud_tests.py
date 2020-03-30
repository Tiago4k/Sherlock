import os
import json
import unittest
import requests

with open(os.getcwd() + '/Unit Tests/config.json', 'r') as config:
    data = config.read()

config_data = json.loads(data)

get_url = str(config_data['get_url'])
ela_url = str(config_data['ela_url'])
post_url = str(config_data['post_url'])
router_url = str(config_data['router_url'])
resize_url = str(config_data['resize_url'])
download_url = str(config_data['download_url'])
prediction_url = str(config_data['prediction_url'])
send_to_bucket_url = str(config_data['send_to_bucket_url'])
bucket_name = str(config_data['bucket_name'])


class TestBucket(unittest.TestCase):

    def test_send_to_bucket(self):
        """
        Test send_to_bucket cloud function.
        """

        with open(os.getcwd() + '/Unit Tests/Assets/base64.json', 'r') as base64:
            data = base64.read()

        base64_img = json.loads(data)

        payload = {
            'bucket_dir': 'ORIGINALS',
            'bucket_name': bucket_name,
            'img_bytes': str(base64_img['base64_img']),
            'uuid': 'unit-testing-bucket'
        }

        response = requests.post(send_to_bucket_url, json=payload).json()
        self.assertEqual(response['status'], 201)


class TestDownload(unittest.TestCase):

    def test_download_img(self):
        """
        Test download_img cloud function.
        """

        payload = {
            'bucket_name': bucket_name,
            'filepath': 'ORIGINALS/unit-testing-bucket'
        }

        download_resp = requests.post(download_url, json=payload).json()
        self.assertEqual(download_resp['status'], 200)


class TestResize(unittest.TestCase):

    def test_resize(self):

        with open(os.getcwd() + '/Unit Tests/Assets/base64.json', 'r') as base64:
            data = base64.read()

        base64_img = json.loads(data)

        payload = {
            'bucket_name': bucket_name,
            'img_bytes': str(base64_img['base64_img']),
            'uuid': 'unit-testing-resize'
        }

        response = requests.post(resize_url, json=payload).json()
        self.assertEqual(response['status'], 200)


class TestFirestore(unittest.TestCase):

    def test_post(self):
        """
        Test post_to_firestore http request.
        """

        payload = {
            'uuid': 'unit-testing-post',
            'username': 'unit_testing@test.com',
            'prediction': 'Authentic',
            'confidence': '93.3',
            'bucket_name': bucket_name
        }

        response = requests.post(post_url, json=payload).json()
        self.assertEqual(response['status'], 201)

    def test_get(self):
        """
        Test get_from_firestore http request.
        """

        payload = {
            'username': 'unit_testing@test.com'
        }

        response = requests.post(get_url, json=payload).json()
        self.assertEqual(response['status'], 200)


class TestAPIs(unittest.TestCase):

    def test_ela_api(self):
        """
        Test to see if an ELA image is produced by the ELA_API.
        If successful, a 200 response will be returned.
        """

        with open(os.getcwd() + '/Unit Tests/Assets/base64.json', 'r') as base64:
            data = base64.read()

        base64_img = json.loads(data)

        payload = {
            'uuid': 'testing-ela-api',
            'bucket_name': bucket_name,
            'img_bytes': str(base64_img['base64_img'])
        }

        response = requests.post(ela_url, json=payload).json()
        self.assertEqual(response['status'], 200)

    def test_prediction_api(self):
        """
        Test to see if a prediction is produced by the Prediction_API.
        If successful, a 200 response will be returned.
        """

        with open(os.getcwd() + '/Unit Tests/Assets/base64.json', 'r') as base64:
            data = base64.read()

        base64_img = json.loads(data)

        payload = {
            'uuid': 'testing-ela-api',
            'img_bytes': str(base64_img['base64_img'])
        }

        response = requests.post(prediction_url, json=payload).json()
        self.assertEqual(response['Status'], 200)

    def test_post_router_api(self):
        """
        Test to see if the router carries out it's instructions. 
        If successful, a 200 response will be returned.
        """

        with open(os.getcwd() + '/Unit Tests/Assets/base64.json', 'r') as base64:
            data = base64.read()

        base64_img = json.loads(data)

        payload = {
            'file': 'data:application/octet-stream;base64,' + str(base64_img['base64_img']),
            'email': 'unit_testing@test.com'
        }

        response = requests.post(router_url, json=payload).json()

        self.assertEqual(response['status'], 200)

    def test_post_router_bad_request(self):
        """
        Test to see if the router raises a bad request error.
        Produced by not sending the API an image
        """

        payload = {
            'email': '',
            'file': ''
        }

        response = requests.post(router_url, json=payload).json()

        self.assertEqual(response['message'], 'Internal Server Error')

    def test_get_router_api(self):
        """
        Test to see if a router is returns a list of all the images a user has uploaded.
        If successful, a 200 response will be returned.
        """

        r = requests.get(router_url + '/user/' +
                         'unit_testing%40test.com').json()

        self.assertEqual(r['status'], 200)


if __name__ == "__main__":

    unittest.main()
