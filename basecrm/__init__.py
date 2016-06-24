"""
BaseCRM official API V2 library client for Python.
~~~~~~~~~~~~~~~~~~~~~

Usage::

  >>> import os
  >>> import basecrm
  >>> client = basecrm.Client(access_token=os.environ.get('BASECRM_ACCESS_TOKEN')
  >>> coffeeshop = client.contacts.create(name='Coffee Shop', is_organization=True)
  >>> chemex = client.deals.create(name='Chemex', contact_id=coffeeshop.id, value=99, currency='USD')
  >>> print chemex.hot

:copyright: (c) 2016 by BaseCRM developers (developers@getbase.com).
:license: MIT, see LICENSE for more details.
"""

from basecrm.version import VERSION
from basecrm.errors import (
    ConfigurationError,
    RateLimitError,
    BaseError,
    RequestError,
    ResourceError,
    ServerError
)

from basecrm.configuration import Configuration
from basecrm.http_client import HttpClient

from basecrm.services import (
    AccountsService,
    AssociatedContactsService,
    ContactsService,
    DealsService,
    LeadsService,
    LossReasonsService,
    NotesService,
    PipelinesService,
    SourcesService,
    StagesService,
    TagsService,
    TasksService,
    UsersService,
)

from basecrm.sync import (
    SyncService,
    Sync
)

from basecrm.client import Client
