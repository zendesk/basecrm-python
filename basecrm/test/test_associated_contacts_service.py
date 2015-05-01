import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class AssociatedContactsServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'associated_contacts'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.associated_contacts, 'list') and callable(getattr(self.client.associated_contacts, 'list')))

    def test_method_create_exists(self):
        self.assertTrue(hasattr(self.client.associated_contacts, 'create') and callable(getattr(self.client.associated_contacts, 'create')))

    def test_method_destroy_exists(self):
        self.assertTrue(hasattr(self.client.associated_contacts, 'destroy') and callable(getattr(self.client.associated_contacts, 'destroy')))

    def test_list(self):
        associated_contacts = self.client.associated_contacts.list(self.associated_contact.deal_id, page=1)
        self.assertIsInstance(associated_contacts, list)
        for associated_contact in associated_contacts:
            self.assertIsInstance(associated_contact, munch.Munch)
 

    def test_create(self):
        self.assertIsInstance(self.associated_contact, munch.Munch)
        self.assertGreaterEqual(len(self.associated_contact), 1)
 

    def test_destroy(self):
        new_associated_contact = self.create_associated_contact()
        self.assertTrue(self.client.associated_contacts.destroy(new_associated_contact.deal_id, new_associated_contact.contact_id))
 
