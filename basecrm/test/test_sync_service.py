import munch

try:
    from unittest import mock
except ImportError:
    import mock

import basecrm
from basecrm.test.testutils import BaseTestCase
from munch import munchify


class SyncServiceTests(BaseTestCase):
    @property
    def device_uuid(self):
        return '6dadcec8-6e61-4691-b318-1aab27b8fecf'

    def session_id(self):
        return '29f2aeeb-8d68-4ea7-95c3-a2c8e151f5a3'

    def test_service_property_exists(self):
        self.assertTrue(hasattr(self.client, 'sync'))

    def test_method_start_exists(self):
        self.assertTrue(hasattr(self.client.sync, 'start') and
                        callable(getattr(self.client.sync, 'start')))

    def test_method_fetch_exists(self):
        self.assertTrue(hasattr(self.client.sync, 'fetch') and
                        callable(getattr(self.client.sync, 'fetch')))

    def test_method_ack_exists(self):
        self.assertTrue(hasattr(self.client.sync, 'ack') and
                        callable(getattr(self.client.sync, 'ack')))

    def test_start_nothing_new(self):
        http_client = mock.create_autospec(basecrm.HttpClient)
        http_client.post.return_value = (204, {}, None)

        sync = basecrm.SyncService(http_client)
        self.assertEquals(sync.start(self.device_uuid), None)
        http_client.post.assert_called_once_with('/sync/start',
                                                 body=None,
                                                 headers={'X-Basecrm-Device-UUID': self.device_uuid})

    def test_start_got_session(self):
        session = munch.Munch(id=self.session_id)
        http_client = mock.create_autospec(basecrm.HttpClient)
        http_client.post.return_value = (200, {}, session)

        sync = basecrm.SyncService(http_client)
        self.assertEquals(sync.start(self.device_uuid), session)
        http_client.post.assert_called_once_with('/sync/start',
                                                 body=None,
                                                 headers={'X-Basecrm-Device-UUID': self.device_uuid})

    def test_ack(self):
        ack_keys = ['User-1234-1', 'Source-1234-1']
        http_client = mock.create_autospec(basecrm.HttpClient)
        http_client.post.return_value = (202, {}, None)

        sync = basecrm.SyncService(http_client)
        self.assertTrue(sync.ack(self.device_uuid, ack_keys))
        http_client.post.assert_called_once_with('/sync/ack',
                                                 body={'ack_keys': ack_keys},
                                                 headers={'X-Basecrm-Device-UUID': self.device_uuid})

    def test_fetch_no_more_data(self):
        http_client = mock.create_autospec(basecrm.HttpClient)
        http_client.get.return_value = (204, {}, None)

        sync = basecrm.SyncService(http_client)
        self.assertEquals(sync.fetch(self.device_uuid, self.session_id), [])
        http_client.get.assert_called_once_with("/sync/{session_id}/queues/main".format(session_id=self.session_id),
                                                params=None,
                                                headers={'X-Basecrm-Device-UUID': self.device_uuid},
                                                raw=True)

    def test_fetch_got_data(self):
        queue_items = munchify({
            'items': [{
                'data': {
                    'id': 1
                },
                'meta': {
                    'type': 'user',
                    'sync': {
                        'event_type': 'created',
                        'ack_key': 'User-1234-1',
                        'revision': 1
                    }
                }
            }]
        })
        http_client = mock.create_autospec(basecrm.HttpClient)
        http_client.get.return_value = (200, {}, queue_items)

        sync = basecrm.SyncService(http_client)
        self.assertEquals(sync.fetch(self.device_uuid, self.session_id), queue_items['items'])
        http_client.get.assert_called_once_with("/sync/{session_id}/queues/main".format(session_id=self.session_id),
                                                params=None,
                                                headers={'X-Basecrm-Device-UUID': self.device_uuid},
                                                raw=True)
