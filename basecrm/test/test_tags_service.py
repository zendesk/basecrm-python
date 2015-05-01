import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class TagsServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'tags'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.tags, 'list') and callable(getattr(self.client.tags, 'list')))

    def test_method_create_exists(self):
        self.assertTrue(hasattr(self.client.tags, 'create') and callable(getattr(self.client.tags, 'create')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.tags, 'retrieve') and callable(getattr(self.client.tags, 'retrieve')))

    def test_method_update_exists(self):
        self.assertTrue(hasattr(self.client.tags, 'update') and callable(getattr(self.client.tags, 'update')))

    def test_method_destroy_exists(self):
        self.assertTrue(hasattr(self.client.tags, 'destroy') and callable(getattr(self.client.tags, 'destroy')))

    def test_list(self):
        tags = self.client.tags.list(page=1)
        self.assertIsInstance(tags, list)
        for tag in tags:
            self.assertIsInstance(tag, munch.Munch)
 

    def test_create(self):
        self.assertIsInstance(self.tag, munch.Munch)
        self.assertGreaterEqual(len(self.tag), 1)
 

    def test_retrieve(self):
        found_tag = self.client.tags.retrieve(self.tag.id);
        self.assertIsInstance(found_tag, munch.Munch);
        self.assertEqual(found_tag.id, self.tag.id);
 

    def test_update(self):
        updated_tag = self.client.tags.update(self.tag.id, self.tag)
        self.assertIsInstance(updated_tag, munch.Munch)
        self.assertGreaterEqual(len(updated_tag), 1)
 

    def test_destroy(self):
        new_tag = self.create_tag()
        self.assertTrue(self.client.tags.destroy(new_tag.id))
 
