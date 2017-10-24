import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class OrdersServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'orders'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.orders, 'list') and callable(getattr(self.client.orders, 'list')))

    def test_method_create_exists(self):
        self.assertTrue(hasattr(self.client.orders, 'create') and callable(getattr(self.client.orders, 'create')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.orders, 'retrieve') and callable(getattr(self.client.orders, 'retrieve')))

    def test_method_update_exists(self):
        self.assertTrue(hasattr(self.client.orders, 'update') and callable(getattr(self.client.orders, 'update')))

    def test_method_destroy_exists(self):
        self.assertTrue(hasattr(self.client.orders, 'destroy') and callable(getattr(self.client.orders, 'destroy')))

    def test_list(self):
        orders = self.client.orders.list(page=1)
        self.assertIsInstance(orders, list)
        for order in orders:
            self.assertIsInstance(order, munch.Munch)
 

    def test_create(self):
        self.assertIsInstance(self.order, munch.Munch)
        self.assertGreaterEqual(len(self.order), 1)
 

    def test_retrieve(self):
        found_order = self.client.orders.retrieve(self.order.id);
        self.assertIsInstance(found_order, munch.Munch);
        self.assertEqual(found_order.id, self.order.id);
 

    def test_update(self):
        updated_order = self.client.orders.update(self.order.id, self.order)
        self.assertIsInstance(updated_order, munch.Munch)
        self.assertGreaterEqual(len(updated_order), 1)
 

    def test_destroy(self):
        new_order = self.create_order()
        self.assertTrue(self.client.orders.destroy(new_order.id))
 
