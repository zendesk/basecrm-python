import basecrm
from basecrm.test.testutils import BaseTestCase
from requests.exceptions import ConnectionError


class HttpClientTests(BaseTestCase):
    @property
    def http_client(self):
        return self.client.http_client

    def test_invalid_request_error(self):
        try:
            self.http_client.get("/users/self", params={'unknown': 'param'})
        except basecrm.RequestError as exception:
            self.assertEqual(exception.http_status, 400)
            self.assertGreaterEqual(len(exception.logref), 1)
            self.assertIsInstance(exception.errors, list)
            self.assertGreaterEqual(len(exception.errors), 1)
        except Exception as e:
            self.fail("Unexpected exception type %r" % type(e))
        else:
            self.fail("Exception expected")

    def test_invalid_payload_error(self):
        try:
            self.http_client.post("/deals", body={'unknown': 'attribute'})
        except basecrm.ResourceError as exception:
            self.assertEqual(exception.http_status, 422)
            self.assertGreaterEqual(len(exception.logref), 1)
            self.assertIsInstance(exception.errors, list)
            self.assertGreaterEqual(len(exception.errors), 1)
        except Exception as e:
            self.fail("Unexpected exception type %r" % type(e))
        else:
            self.fail("Exception expected")

    def test_authentication_error(self):
        http_client = basecrm.Client(access_token='X'*64,
                                     user_agent=self.user_agent,
                                     verbose=True).http_client

        try:
            http_client.get("/users/self")
        except basecrm.RequestError as exception:
            self.assertEqual(exception.http_status, 401)
            self.assertGreaterEqual(len(exception.logref), 1)
            self.assertIsInstance(exception.errors, list)
            self.assertGreaterEqual(len(exception.errors), 1)
        except Exception as e:
            self.fail("Unexpected exception type %r" % type(e))
        else:
            self.fail("Exception expected")

    def test_connection_error(self):
        http_client = basecrm.Client(access_token='X'*64,
                                     base_url='https://somethingthatnotexist.fail',
                                     user_agent=self.user_agent,
                                     verbose=True).http_client

        try:
            http_client.get("/users/self")
        except ConnectionError as e:
            # OK
            self.assertTrue(True)
        except Exception as e:
            self.fail("Unexpected exception type %r" % type(e))
        else:
            self.fail("Exception expected")
