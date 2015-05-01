import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class ContactsServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'contacts'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.contacts, 'list') and callable(getattr(self.client.contacts, 'list')))

    def test_method_create_exists(self):
        self.assertTrue(hasattr(self.client.contacts, 'create') and callable(getattr(self.client.contacts, 'create')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.contacts, 'retrieve') and callable(getattr(self.client.contacts, 'retrieve')))

    def test_method_update_exists(self):
        self.assertTrue(hasattr(self.client.contacts, 'update') and callable(getattr(self.client.contacts, 'update')))

    def test_method_destroy_exists(self):
        self.assertTrue(hasattr(self.client.contacts, 'destroy') and callable(getattr(self.client.contacts, 'destroy')))

    def test_list(self):
        contacts = self.client.contacts.list(page=1)
        self.assertIsInstance(contacts, list)
        for contact in contacts:
            self.assertIsInstance(contact, munch.Munch)
 

    def test_create(self):
        self.assertIsInstance(self.contact, munch.Munch)
        self.assertGreaterEqual(len(self.contact), 1)
 

    def test_retrieve(self):
        found_contact = self.client.contacts.retrieve(self.contact.id);
        self.assertIsInstance(found_contact, munch.Munch);
        self.assertEqual(found_contact.id, self.contact.id);
 

    def test_update(self):
        updated_contact = self.client.contacts.update(self.contact.id, self.contact)
        self.assertIsInstance(updated_contact, munch.Munch)
        self.assertGreaterEqual(len(updated_contact), 1)
 

    def test_destroy(self):
        new_contact = self.create_contact()
        self.assertTrue(self.client.contacts.destroy(new_contact.id))
 
