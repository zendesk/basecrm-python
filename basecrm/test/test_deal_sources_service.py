import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class DealSourcesServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'deal_sources'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.deal_sources, 'list') and callable(getattr(self.client.deal_sources, 'list')))

    def test_method_create_exists(self):
        self.assertTrue(hasattr(self.client.deal_sources, 'create') and callable(getattr(self.client.deal_sources, 'create')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.deal_sources, 'retrieve') and callable(getattr(self.client.deal_sources, 'retrieve')))

    def test_method_update_exists(self):
        self.assertTrue(hasattr(self.client.deal_sources, 'update') and callable(getattr(self.client.deal_sources, 'update')))

    def test_method_destroy_exists(self):
        self.assertTrue(hasattr(self.client.deal_sources, 'destroy') and callable(getattr(self.client.deal_sources, 'destroy')))

    def test_list(self):
        deal_sources = self.client.deal_sources.list(page=1)
        self.assertIsInstance(deal_sources, list)
        for deal_source in deal_sources:
            self.assertIsInstance(deal_source, munch.Munch)
 

    def test_create(self):
        self.assertIsInstance(self.deal_source, munch.Munch)
        self.assertGreaterEqual(len(self.deal_source), 1)
 

    def test_retrieve(self):
        found_deal_source = self.client.deal_sources.retrieve(self.deal_source.id);
        self.assertIsInstance(found_deal_source, munch.Munch);
        self.assertEqual(found_deal_source.id, self.deal_source.id);
 

    def test_update(self):
        updated_deal_source = self.client.deal_sources.update(self.deal_source.id, self.deal_source)
        self.assertIsInstance(updated_deal_source, munch.Munch)
        self.assertGreaterEqual(len(updated_deal_source), 1)
 

    def test_destroy(self):
        new_deal_source = self.create_deal_source()
        self.assertTrue(self.client.deal_sources.destroy(new_deal_source.id))
 
