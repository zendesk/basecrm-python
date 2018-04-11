import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class LeadUnqualifiedReasonsServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'lead_unqualified_reasons'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.lead_unqualified_reasons, 'list') and callable(getattr(self.client.lead_unqualified_reasons, 'list')))

    def test_list(self):
        lead_unqualified_reasons = self.client.lead_unqualified_reasons.list(page=1)
        self.assertIsInstance(lead_unqualified_reasons, list)
        for lead_unqualified_reason in lead_unqualified_reasons:
            self.assertIsInstance(lead_unqualified_reason, munch.Munch)
 
