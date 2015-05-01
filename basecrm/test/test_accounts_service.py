import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class AccountsServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'accounts'))

    def test_method_self_exists(self):
        self.assertTrue(hasattr(self.client.accounts, 'self') and callable(getattr(self.client.accounts, 'self')))

    def test_self(self):
        resource = self.client.accounts.self()
        self.assertIsInstance(resource, munch.Munch)
 
