import basecrm
from basecrm.test.testutils import BaseTestCase
from requests.exceptions import ConnectionError

class HttpClientTests(BaseTestCase):
    @property
    def http_client(self):
        return self.client.http_client

    def test_invalid_request_error(self):
        with self.assertRaises(basecrm.RequestError) as cm:
            self.http_client.get("/users/self", params={'unknown': 'param'})

        exception = cm.exception

        self.assertEqual(exception.http_status, 400)
        self.assertGreaterEqual(len(exception.logref), 1)
        self.assertIsInstance(exception.errors, list)
        self.assertGreaterEqual(len(exception.errors), 1)

    def test_invalid_payload_error(self):
        with self.assertRaises(basecrm.ResourceError) as cm:
            self.http_client.post("/deals", body={'unknown': 'attribute'})

        exception = cm.exception

        self.assertEqual(exception.http_status, 422)
        self.assertGreaterEqual(len(exception.logref), 1)
        self.assertIsInstance(exception.errors, list)
        self.assertGreaterEqual(len(exception.errors), 1)

    def test_authentication_error(self):
        http_client = basecrm.Client(access_token='X'*64,
                                     user_agent=self.user_agent,
                                     verbose=True).http_client

        with self.assertRaises(basecrm.RequestError) as cm:
            http_client.get("/users/self")

        exception = cm.exception

        self.assertEqual(exception.http_status, 401)
        self.assertGreaterEqual(len(exception.logref), 1)
        self.assertIsInstance(exception.errors, list)
        self.assertGreaterEqual(len(exception.errors), 1)

    def test_connection_error(self):
        http_client = basecrm.Client(access_token='X'*64,
                                     base_url='https://somethingthatnotexist.fail',
                                     user_agent=self.user_agent,
                                     verbose=True).http_client

        with self.assertRaises(ConnectionError):
            http_client.get("/users/self")
