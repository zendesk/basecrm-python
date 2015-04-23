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

from basecrm.client import Client
