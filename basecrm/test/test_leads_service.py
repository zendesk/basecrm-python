import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class LeadsServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'leads'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.leads, 'list') and callable(getattr(self.client.leads, 'list')))

    def test_method_create_exists(self):
        self.assertTrue(hasattr(self.client.leads, 'create') and callable(getattr(self.client.leads, 'create')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.leads, 'retrieve') and callable(getattr(self.client.leads, 'retrieve')))

    def test_method_update_exists(self):
        self.assertTrue(hasattr(self.client.leads, 'update') and callable(getattr(self.client.leads, 'update')))

    def test_method_destroy_exists(self):
        self.assertTrue(hasattr(self.client.leads, 'destroy') and callable(getattr(self.client.leads, 'destroy')))

    def test_list(self):
        leads = self.client.leads.list(page=1)
        self.assertIsInstance(leads, list)
        for lead in leads:
            self.assertIsInstance(lead, munch.Munch)
 

    def test_create(self):
        self.assertIsInstance(self.lead, munch.Munch)
        self.assertGreaterEqual(len(self.lead), 1)
 

    def test_retrieve(self):
        found_lead = self.client.leads.retrieve(self.lead.id);
        self.assertIsInstance(found_lead, munch.Munch);
        self.assertEqual(found_lead.id, self.lead.id);
 

    def test_update(self):
        updated_lead = self.client.leads.update(self.lead.id, self.lead)
        self.assertIsInstance(updated_lead, munch.Munch)
        self.assertGreaterEqual(len(updated_lead), 1)
 

    def test_destroy(self):
        new_lead = self.create_lead()
        self.assertTrue(self.client.leads.destroy(new_lead.id))
 
