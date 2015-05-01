import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class StagesServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'stages'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.stages, 'list') and callable(getattr(self.client.stages, 'list')))

    def test_list(self):
        stages = self.client.stages.list(page=1)
        self.assertIsInstance(stages, list)
        for stage in stages:
            self.assertIsInstance(stage, munch.Munch)
 
