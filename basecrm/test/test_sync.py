import munch

try:
    from unittest import mock
except ImportError:
    import mock

import basecrm
from basecrm.test.testutils import BaseTestCase
from munch import munchify


class SyncTests(BaseTestCase):
    @property
    def device_uuid(self):
        return '6dadcec8-6e61-4691-b318-1aab27b8fecf'

    def session_id(self):
        return '29f2aeeb-8d68-4ea7-95c3-a2c8e151f5a3'

    def test_method_fetch_exists(self):
        sync = basecrm.Sync(self.client, self.device_uuid)
        self.assertTrue(hasattr(sync, 'fetch') and
                        callable(getattr(sync, 'fetch')))

    def test_synchronization_flow_nothing_new(self):
        client = mock.create_autospec(basecrm.Client)
        sync_service = mock.create_autospec(basecrm.SyncService)
        sync_service.start.return_value = None

        client.sync = sync_service

        sync = basecrm.Sync(client, self.device_uuid)
        sync.fetch(lambda meta, data: basecrm.Sync.ACK)

        sync_service.start.assert_called_once_with(self.device_uuid)

    def test_synchronization_flow(self):
        session = {
            'id': self.session_id
        }

        queue_items = [{
            'data': {
                'id': 1,
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

        client = mock.create_autospec(basecrm.Client)
        sync_service = mock.create_autospec(basecrm.SyncService)
        sync_service.start.return_value = session
        sync_service.fetch.side_effect = [queue_items, []]
        sync_service.ack.return_value = True

        client.sync = sync_service

        sync = basecrm.Sync(client, self.device_uuid)
        sync.fetch(lambda meta, data: basecrm.Sync.ACK)


        sync_service.start.assert_called_once_with(self.device_uuid)
        sync_service.fetch.assert_has_calls([mock.call(self.device_uuid, self.session_id),
                                             mock.call(self.device_uuid, self.session_id)])
        sync_service.ack.assert_called_once_with(self.device_uuid, ['User-1234-1'])
