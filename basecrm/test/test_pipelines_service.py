import unittest
import munch

import basecrm 
from basecrm.test.testutils import BaseTestCase

class PipelinesServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'pipelines'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.pipelines, 'list') and callable(getattr(self.client.pipelines, 'list')))

    def test_list(self):
        pipelines = self.client.pipelines.list(page=1)
        self.assertIsInstance(pipelines, list)
        for pipeline in pipelines:
            self.assertIsInstance(pipeline, munch.Munch)
 
