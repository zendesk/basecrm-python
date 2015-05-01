import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class UsersServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'users'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.users, 'list') and callable(getattr(self.client.users, 'list')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.users, 'retrieve') and callable(getattr(self.client.users, 'retrieve')))

    def test_method_self_exists(self):
        self.assertTrue(hasattr(self.client.users, 'self') and callable(getattr(self.client.users, 'self')))

    def test_list(self):
        users = self.client.users.list(page=1)
        self.assertIsInstance(users, list)
        for user in users:
            self.assertIsInstance(user, munch.Munch)
 

    def test_retrieve(self):
        found_user = self.client.users.retrieve(self.user.id);
        self.assertIsInstance(found_user, munch.Munch);
        self.assertEqual(found_user.id, self.user.id);
 

    def test_self(self):
        resource = self.client.users.self()
        self.assertIsInstance(resource, munch.Munch)
 
