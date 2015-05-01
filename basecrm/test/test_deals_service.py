import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class DealsServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'deals'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.deals, 'list') and callable(getattr(self.client.deals, 'list')))

    def test_method_create_exists(self):
        self.assertTrue(hasattr(self.client.deals, 'create') and callable(getattr(self.client.deals, 'create')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.deals, 'retrieve') and callable(getattr(self.client.deals, 'retrieve')))

    def test_method_update_exists(self):
        self.assertTrue(hasattr(self.client.deals, 'update') and callable(getattr(self.client.deals, 'update')))

    def test_method_destroy_exists(self):
        self.assertTrue(hasattr(self.client.deals, 'destroy') and callable(getattr(self.client.deals, 'destroy')))

    def test_list(self):
        deals = self.client.deals.list(page=1)
        self.assertIsInstance(deals, list)
        for deal in deals:
            self.assertIsInstance(deal, munch.Munch)
 

    def test_create(self):
        self.assertIsInstance(self.deal, munch.Munch)
        self.assertGreaterEqual(len(self.deal), 1)
 

    def test_retrieve(self):
        found_deal = self.client.deals.retrieve(self.deal.id);
        self.assertIsInstance(found_deal, munch.Munch);
        self.assertEqual(found_deal.id, self.deal.id);
 

    def test_update(self):
        updated_deal = self.client.deals.update(self.deal.id, self.deal)
        self.assertIsInstance(updated_deal, munch.Munch)
        self.assertGreaterEqual(len(updated_deal), 1)
 

    def test_destroy(self):
        new_deal = self.create_deal()
        self.assertTrue(self.client.deals.destroy(new_deal.id))
 
