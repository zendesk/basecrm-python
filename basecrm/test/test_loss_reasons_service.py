import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class LossReasonsServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'loss_reasons'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.loss_reasons, 'list') and callable(getattr(self.client.loss_reasons, 'list')))

    def test_method_create_exists(self):
        self.assertTrue(hasattr(self.client.loss_reasons, 'create') and callable(getattr(self.client.loss_reasons, 'create')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.loss_reasons, 'retrieve') and callable(getattr(self.client.loss_reasons, 'retrieve')))

    def test_method_update_exists(self):
        self.assertTrue(hasattr(self.client.loss_reasons, 'update') and callable(getattr(self.client.loss_reasons, 'update')))

    def test_method_destroy_exists(self):
        self.assertTrue(hasattr(self.client.loss_reasons, 'destroy') and callable(getattr(self.client.loss_reasons, 'destroy')))

    def test_list(self):
        loss_reasons = self.client.loss_reasons.list(page=1)
        self.assertIsInstance(loss_reasons, list)
        for loss_reason in loss_reasons:
            self.assertIsInstance(loss_reason, munch.Munch)
 

    def test_create(self):
        self.assertIsInstance(self.loss_reason, munch.Munch)
        self.assertGreaterEqual(len(self.loss_reason), 1)
 

    def test_retrieve(self):
        found_loss_reason = self.client.loss_reasons.retrieve(self.loss_reason.id);
        self.assertIsInstance(found_loss_reason, munch.Munch);
        self.assertEqual(found_loss_reason.id, self.loss_reason.id);
 

    def test_update(self):
        updated_loss_reason = self.client.loss_reasons.update(self.loss_reason.id, self.loss_reason)
        self.assertIsInstance(updated_loss_reason, munch.Munch)
        self.assertGreaterEqual(len(updated_loss_reason), 1)
 

    def test_destroy(self):
        new_loss_reason = self.create_loss_reason()
        self.assertTrue(self.client.loss_reasons.destroy(new_loss_reason.id))
 
