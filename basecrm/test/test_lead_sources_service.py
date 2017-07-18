import munch

from basecrm.test.testutils import BaseTestCase

class LeadSourcesServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'lead_sources'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.lead_sources, 'list') and callable(getattr(self.client.lead_sources, 'list')))

    def test_method_create_exists(self):
        self.assertTrue(hasattr(self.client.lead_sources, 'create') and callable(getattr(self.client.lead_sources, 'create')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.lead_sources, 'retrieve') and callable(getattr(self.client.lead_sources, 'retrieve')))

    def test_method_update_exists(self):
        self.assertTrue(hasattr(self.client.lead_sources, 'update') and callable(getattr(self.client.lead_sources, 'update')))

    def test_method_destroy_exists(self):
        self.assertTrue(hasattr(self.client.lead_sources, 'destroy') and callable(getattr(self.client.lead_sources, 'destroy')))

    def test_list(self):
        sources = self.client.lead_sources.list(page=1)
        self.assertIsInstance(sources, list)
        for source in sources:
            self.assertIsInstance(source, munch.Munch)


    def test_create(self):
        self.assertIsInstance(self.lead_source, munch.Munch)
        self.assertGreaterEqual(len(self.lead_source), 1)


    def test_retrieve(self):
        found_source = self.client.lead_sources.retrieve(self.lead_source.id);
        self.assertIsInstance(found_source, munch.Munch);
        self.assertEqual(found_source.id, self.source.id);


    def test_update(self):
        updated_source = self.client.lead_sources.update(self.lead_source.id, self.lead_source)
        self.assertIsInstance(updated_source, munch.Munch)
        self.assertGreaterEqual(len(updated_source), 1)


    def test_destroy(self):
        new_source = self.create_lead_source()
        self.assertTrue(self.client.lead_sources.destroy(new_source.id))
