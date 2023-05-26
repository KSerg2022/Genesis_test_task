import os
import unittest
import requests

from app.main.json_file import JsonFile


class TestApi(unittest.TestCase):

    def setUp(self) -> None:
        self.host = 'http://127.0.0.1:5000'

    def method_disable(self, method, url):
        """HTTP method POST."""
        response = self.get_response(method, url)
        if method == 'GET':
            self.assertEqual(list(response.values())[0], 'method "GET" is disable.')
        elif method == 'POST':
            self.assertEqual(list(response.values())[0], 'method "POST" is disable.')
        elif method == 'PUT':
            self.assertEqual(list(response.values())[0], 'method "PUT" is disable.')
        else:
            self.assertEqual(list(response.values())[0], 'method "DELETE" is disable.')

    @staticmethod
    def get_response(method, url, headers=None, json=None):
        return requests.request(method,
                                url=url,
                                headers=headers,
                                json=json).json()


class TestBtc(TestApi):

    def setUp(self) -> None:
        super().setUp()
        self.url = self.host + '/api/rate/'

    def test_btc_get(self):
        response = self.get_response('GET', self.url)
        self.assertEqual(list(response.keys())[0], 'rate')
        self.assertIsInstance(list(response.values())[0], float)

    def test_btc_post(self):
        self.method_disable('POST', self.url)

    def test_btc_put(self):
        self.method_disable('PUT', self.url)

    def test_btc_delete(self):
        self.method_disable('DELETE', self.url)


class TestEmail(TestApi):

    def setUp(self) -> None:
        super().setUp()
        self.url = self.host + '/api/subscribe/'
        self.headers = {'Content-Type': 'application/json'
                        }

    def test_email_get(self):
        self.method_disable('GET', self.url)

    def test_email_post(self):
        json = JsonFile()
        os.remove(json.path_to_file)

        response = self.get_response('POST',
                                     self.url,
                                     self.headers,
                                     {'name': 'first@gmail.com'
                                      })

        self.assertEqual(list(response.keys())[0], 'message')
        self.assertEqual(list(response.values())[0], 'E-mail додано')

    def test_email_post_duplicate(self):
        email = {'name': 'second@gmail.com'}
        response = self.get_response('POST', self.url, self.headers, email)
        self.assertEqual(list(response.keys())[0], 'message')
        self.assertEqual(list(response.values())[0], 'E-mail додано')

        response = self.get_response('POST', self.url, self.headers, email)
        self.assertEqual(list(response.keys())[0], 'message')
        self.assertEqual(list(response.values())[0], 'Повертати, якщо e-mail вже є в базі даних (файловій)')

    def test_email_put(self):
        self.method_disable('PUT', self.url)

    def test_email_delete(self):
        self.method_disable('DELETE', self.url)


class TestSendBtc(TestApi):

    def setUp(self) -> None:
        super().setUp()
        self.url = self.host + '/api/sendEmails/'

    def test_send_email_get(self):
        self.method_disable('GET', self.url)

    def test_send_email_post(self):
        response = self.get_response('POST', self.url)
        self.assertEqual(list(response.values())[0], 'E-mail-и відправлено')

    def test_send_email_put(self):
        self.method_disable('PUT', self.url)

    def test_send_email_delete(self):
        self.method_disable('DELETE', self.url)
