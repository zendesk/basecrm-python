import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class TasksServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'tasks'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.tasks, 'list') and callable(getattr(self.client.tasks, 'list')))

    def test_method_create_exists(self):
        self.assertTrue(hasattr(self.client.tasks, 'create') and callable(getattr(self.client.tasks, 'create')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.tasks, 'retrieve') and callable(getattr(self.client.tasks, 'retrieve')))

    def test_method_update_exists(self):
        self.assertTrue(hasattr(self.client.tasks, 'update') and callable(getattr(self.client.tasks, 'update')))

    def test_method_destroy_exists(self):
        self.assertTrue(hasattr(self.client.tasks, 'destroy') and callable(getattr(self.client.tasks, 'destroy')))

    def test_list(self):
        tasks = self.client.tasks.list(page=1)
        self.assertIsInstance(tasks, list)
        for task in tasks:
            self.assertIsInstance(task, munch.Munch)
 

    def test_create(self):
        self.assertIsInstance(self.task, munch.Munch)
        self.assertGreaterEqual(len(self.task), 1)
 

    def test_retrieve(self):
        found_task = self.client.tasks.retrieve(self.task.id);
        self.assertIsInstance(found_task, munch.Munch);
        self.assertEqual(found_task.id, self.task.id);
 

    def test_update(self):
        updated_task = self.client.tasks.update(self.task.id, self.task)
        self.assertIsInstance(updated_task, munch.Munch)
        self.assertGreaterEqual(len(updated_task), 1)
 

    def test_destroy(self):
        new_task = self.create_task()
        self.assertTrue(self.client.tasks.destroy(new_task.id))
 
