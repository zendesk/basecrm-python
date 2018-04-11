import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class DealUnqualifiedReasonsServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'deal_unqualified_reasons'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.deal_unqualified_reasons, 'list') and callable(getattr(self.client.deal_unqualified_reasons, 'list')))

    def test_method_create_exists(self):
        self.assertTrue(hasattr(self.client.deal_unqualified_reasons, 'create') and callable(getattr(self.client.deal_unqualified_reasons, 'create')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.deal_unqualified_reasons, 'retrieve') and callable(getattr(self.client.deal_unqualified_reasons, 'retrieve')))

    def test_method_update_exists(self):
        self.assertTrue(hasattr(self.client.deal_unqualified_reasons, 'update') and callable(getattr(self.client.deal_unqualified_reasons, 'update')))

    def test_method_destroy_exists(self):
        self.assertTrue(hasattr(self.client.deal_unqualified_reasons, 'destroy') and callable(getattr(self.client.deal_unqualified_reasons, 'destroy')))

    def test_list(self):
        deal_unqualified_reasons = self.client.deal_unqualified_reasons.list(page=1)
        self.assertIsInstance(deal_unqualified_reasons, list)
        for deal_unqualified_reason in deal_unqualified_reasons:
            self.assertIsInstance(deal_unqualified_reason, munch.Munch)
 

    def test_create(self):
        self.assertIsInstance(self.deal_unqualified_reason, munch.Munch)
        self.assertGreaterEqual(len(self.deal_unqualified_reason), 1)
 

    def test_retrieve(self):
        found_deal_unqualified_reason = self.client.deal_unqualified_reasons.retrieve(self.deal_unqualified_reason.id);
        self.assertIsInstance(found_deal_unqualified_reason, munch.Munch);
        self.assertEqual(found_deal_unqualified_reason.id, self.deal_unqualified_reason.id);
 

    def test_update(self):
        updated_deal_unqualified_reason = self.client.deal_unqualified_reasons.update(self.deal_unqualified_reason.id, self.deal_unqualified_reason)
        self.assertIsInstance(updated_deal_unqualified_reason, munch.Munch)
        self.assertGreaterEqual(len(updated_deal_unqualified_reason), 1)
 

    def test_destroy(self):
        new_deal_unqualified_reason = self.create_deal_unqualified_reason()
        self.assertTrue(self.client.deal_unqualified_reasons.destroy(new_deal_unqualified_reason.id))
 
