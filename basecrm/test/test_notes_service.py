import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class NotesServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'notes'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.notes, 'list') and callable(getattr(self.client.notes, 'list')))

    def test_method_create_exists(self):
        self.assertTrue(hasattr(self.client.notes, 'create') and callable(getattr(self.client.notes, 'create')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.notes, 'retrieve') and callable(getattr(self.client.notes, 'retrieve')))

    def test_method_update_exists(self):
        self.assertTrue(hasattr(self.client.notes, 'update') and callable(getattr(self.client.notes, 'update')))

    def test_method_destroy_exists(self):
        self.assertTrue(hasattr(self.client.notes, 'destroy') and callable(getattr(self.client.notes, 'destroy')))

    def test_list(self):
        notes = self.client.notes.list(page=1)
        self.assertIsInstance(notes, list)
        for note in notes:
            self.assertIsInstance(note, munch.Munch)
 

    def test_create(self):
        self.assertIsInstance(self.note, munch.Munch)
        self.assertGreaterEqual(len(self.note), 1)
 

    def test_retrieve(self):
        found_note = self.client.notes.retrieve(self.note.id);
        self.assertIsInstance(found_note, munch.Munch);
        self.assertEqual(found_note.id, self.note.id);
 

    def test_update(self):
        updated_note = self.client.notes.update(self.note.id, self.note)
        self.assertIsInstance(updated_note, munch.Munch)
        self.assertGreaterEqual(len(updated_note), 1)
 

    def test_destroy(self):
        new_note = self.create_note()
        self.assertTrue(self.client.notes.destroy(new_note.id))
 
