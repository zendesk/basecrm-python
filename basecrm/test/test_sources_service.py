import unittest
import bunch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class SourcesServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'sources'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.sources, 'list') and callable(getattr(self.client.sources, 'list')))

    def test_method_create_exists(self):
        self.assertTrue(hasattr(self.client.sources, 'create') and callable(getattr(self.client.sources, 'create')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.sources, 'retrieve') and callable(getattr(self.client.sources, 'retrieve')))

    def test_method_update_exists(self):
        self.assertTrue(hasattr(self.client.sources, 'update') and callable(getattr(self.client.sources, 'update')))

    def test_method_destroy_exists(self):
        self.assertTrue(hasattr(self.client.sources, 'destroy') and callable(getattr(self.client.sources, 'destroy')))

    def test_list(self):
        sources = self.client.sources.list(page=1)
        self.assertIsInstance(sources, list)
        for source in sources:
            self.assertIsInstance(source, bunch.Bunch)
 

    def test_create(self):
        self.assertIsInstance(self.source, bunch.Bunch)
        self.assertGreaterEqual(len(self.source), 1)
 

    def test_retrieve(self):
        found_source = self.client.sources.retrieve(self.source.id);
        self.assertIsInstance(found_source, bunch.Bunch);
        self.assertEqual(found_source.id, self.source.id);
 

    def test_update(self):
        updated_source = self.client.sources.update(self.source.id, self.source)
        self.assertIsInstance(updated_source, bunch.Bunch)
        self.assertGreaterEqual(len(updated_source), 1)
 

    def test_destroy(self):
        new_source = self.create_source()
        self.assertTrue(self.client.sources.destroy(new_source.id))
 
