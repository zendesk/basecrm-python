import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class VisitOutcomesServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'visit_outcomes'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.visit_outcomes, 'list') and callable(getattr(self.client.visit_outcomes, 'list')))

    def test_list(self):
        visit_outcomes = self.client.visit_outcomes.list(page=1)
        self.assertIsInstance(visit_outcomes, list)
        for visit_outcome in visit_outcomes:
            self.assertIsInstance(visit_outcome, munch.Munch)
 
