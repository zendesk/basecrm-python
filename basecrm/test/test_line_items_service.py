import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class LineItemsServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'line_items'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.line_items, 'list') and callable(getattr(self.client.line_items, 'list')))

    def test_method_create_exists(self):
        self.assertTrue(hasattr(self.client.line_items, 'create') and callable(getattr(self.client.line_items, 'create')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.line_items, 'retrieve') and callable(getattr(self.client.line_items, 'retrieve')))

    def test_method_destroy_exists(self):
        self.assertTrue(hasattr(self.client.line_items, 'destroy') and callable(getattr(self.client.line_items, 'destroy')))

    def test_list(self):
        line_items = self.client.line_items.list(self.line_item.order_id, page=1)
        self.assertIsInstance(line_items, list)
        for line_item in line_items:
            self.assertIsInstance(line_item, munch.Munch)
 

    def test_create(self):
        self.assertIsInstance(self.line_item, munch.Munch)
        self.assertGreaterEqual(len(self.line_item), 1)
 

    def test_retrieve(self):
        found_line_item = self.client.line_items.retrieve(self.line_item.order_id, self.line_item.id);
        self.assertIsInstance(found_line_item, munch.Munch);
        self.assertEqual(found_line_item.id, self.line_item.id);
 

    def test_destroy(self):
        new_line_item = self.create_line_item()
        self.assertTrue(self.client.line_items.destroy(new_line_item.order_id, new_line_item.id))
 
