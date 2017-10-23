import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class ProductsServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'products'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.products, 'list') and callable(getattr(self.client.products, 'list')))

    def test_method_create_exists(self):
        self.assertTrue(hasattr(self.client.products, 'create') and callable(getattr(self.client.products, 'create')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.products, 'retrieve') and callable(getattr(self.client.products, 'retrieve')))

    def test_method_update_exists(self):
        self.assertTrue(hasattr(self.client.products, 'update') and callable(getattr(self.client.products, 'update')))

    def test_method_destroy_exists(self):
        self.assertTrue(hasattr(self.client.products, 'destroy') and callable(getattr(self.client.products, 'destroy')))

    def test_list(self):
        products = self.client.products.list(page=1)
        self.assertIsInstance(products, list)
        for product in products:
            self.assertIsInstance(product, munch.Munch)
 

    def test_create(self):
        self.assertIsInstance(self.product, munch.Munch)
        self.assertGreaterEqual(len(self.product), 1)
 

    def test_retrieve(self):
        found_product = self.client.products.retrieve(self.product.id);
        self.assertIsInstance(found_product, munch.Munch);
        self.assertEqual(found_product.id, self.product.id);
 

    def test_update(self):
        updated_product = self.client.products.update(self.product.id, self.product)
        self.assertIsInstance(updated_product, munch.Munch)
        self.assertGreaterEqual(len(updated_product), 1)
 

    def test_destroy(self):
        new_product = self.create_product()
        self.assertTrue(self.client.products.destroy(new_product.id))
 
