import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class VisitsServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'visits'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.visits, 'list') and callable(getattr(self.client.visits, 'list')))

    def test_list(self):
        visits = self.client.visits.list(page=1)
        self.assertIsInstance(visits, list)
        for visit in visits:
            self.assertIsInstance(visit, munch.Munch)
 
