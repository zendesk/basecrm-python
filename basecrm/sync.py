class SyncService(object):
    """
    :class `basecrm.SyncService` is used by :class:`basecrm.Client` to make
    low-level actions to Sync API.

    You can either use :class:`basecrm.SyncService` class directly to interact
    with Sync API using low-level interface or :class:`basecrm.Sync` class
    to interact using high-level wrapper.
    """

    def __init__(self, http_client):
        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client

    def start(self, device_uuid):
        """
        Start synchronization flow

        Starts a new synchronization session.
        This is the first endpoint to call, in order to start a new synchronization session.

        :calls: ``post /sync/start``
        :param string device_uuid: Device's UUID for which to perform synchronization.
        :return: Dictionary that support attribute-style access and represents newely created Synchronization Session or None.
        :rtype: dict
        """

        status_code, _, session = self.http_client.post('/sync/start',
                                                        body=None,
                                                        headers=self.build_headers(device_uuid))

        return None if status_code == 204 else session

    def fetch(self, device_uuid, session_id):
        """
        Get data from queue

        Fetch fresh data from the named queue.
        Using session identifier you call continously the `#fetch` method to drain the named queue.

        :calls: ``get /sync/{session_id}/queues/main``
        :param string device_uuid: Device's UUID for which to perform synchronization.
        :param string session_id: Unique identifier of a synchronization session.
        :param string queue: (optional) Queue name.
        :return: List of dictionaries that support attribute-style access,
            which represent resources (data) and associated meta data (meta).
            Empty list if there is no more data to synchronize.
        :rtype: list
        """

        status_code, _, root = self.http_client.get("/sync/{session_id}/queues/main".format(session_id=session_id),
                                                    params=None,
                                                    headers=self.build_headers(device_uuid),
                                                    raw=True)

        return [] if status_code == 204 else root['items']

    def ack(self, device_uuid, ack_keys):
        """
        Acknowledge received data

        Send acknowledgement keys to let know the Sync service which data you have.
        As you fetch new data, you need to send acknowledgement keys.

        :calls: ``post /sync/ack``
        :param string device_uuid: Device's UUID for which to perform synchronization.
        :param list ack_keys: List of acknowledgement keys.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        attributes = {'ack_keys': ack_keys}
        status_code, _, _ = self.http_client.post('/sync/ack',
                                                  body=attributes,
                                                  headers=self.build_headers(device_uuid))

        return status_code == 202

    def build_headers(self, device_uuid):
        return {'X-Basecrm-Device-UUID': device_uuid}


class Sync(object):
    """
    :class:`basecrm.Sync` is a BaseCRM Sync API v2 high-level wrapper.
    """

    """
    Constant representing acknowledged state.
    """
    ACK = True

    """
    Constant representing not acknowledged state.
    """
    NACK = False

    def __init__(self, client, device_uuid):
        """
        :param :class:`basecrm.Client` client: BaseCRM API v2 client instance.
        :param string device_uuid: Device's UUID for which to perform synchronization.
        """
        self.__client = client
        self.__device_uuid = device_uuid

    @property
    def client(self):
        return self.__client

    @property
    def device_uuid(self):
        return self.__device_uuid

    def fetch(self, callback):
        """
        Perform a full synchronization flow.

        .. code-block:: python
            :linenos:

            >>> client = basecrm.Client(access_token='<YOUR_PERSONAL_ACCESS_TOKEN>')
            >>> sync = basecrm.Sync(client=client, device_uuid='<YOUR_DEVICES_UUID>')
            >>> sync.fetch(lambda meta, data: basecrm.Sync.ACK)

        :param callback: Callback that will be called for every item in a queue.
            Takes two input arguments: synchronization meta data and assodicated data.
            It must return either ack or nack.
        """

        # Set up a new synchronization session for a given device's UUID
        session = self.client.sync.start(self.device_uuid)

        # Check if there is anything to synchronize
        if session is None or 'id' not in session:
            return

        # Drain the main queue until there is no more data (empty array)
        while True:
            # Fetch the main queue
            queue_items = self.client.sync.fetch(self.device_uuid, session['id'])

            # nothing more to synchronize ?
            if not queue_items:
                break

            # let client know about both data and meta
            ack_keys = []

            for item in queue_items:
                if callback(item['meta'], item['data']):
                    ack_keys.append(item['meta']['sync']['ack_key'])

            # As we fetch new data, we need to send acknowledgement keys
            # if any ..
            if ack_keys:
                self.client.sync.ack(self.device_uuid, ack_keys)
