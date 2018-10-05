import unittest
import munch

import basecrm
from basecrm.test.testutils import BaseTestCase

class TextMessagesServiceTests(BaseTestCase):
    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'text_messages'))

    def test_method_list_exists(self):
        self.assertTrue(hasattr(self.client.text_messages, 'list') and callable(getattr(self.client.text_messages, 'list')))

    def test_method_retrieve_exists(self):
        self.assertTrue(hasattr(self.client.text_messages, 'retrieve') and callable(getattr(self.client.text_messages, 'retrieve')))

    def test_list(self):
        text_messages = self.client.text_messages.list(page=1)
        self.assertIsInstance(text_messages, list)
        for text_message in text_messages:
            self.assertIsInstance(text_message, munch.Munch)
