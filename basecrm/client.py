from basecrm.configuration import Configuration
from basecrm.http_client import HttpClient
import basecrm.services


class Client(object):
    def __init__(self, **options):
        self.config = Configuration(**options)
        self.config.validate()

        self.http_client = HttpClient(self.config)

        self.__accounts = basecrm.services.AccountsService(self.http_client)
        self.__associated_contacts = basecrm.services.AssociatedContactsService(self.http_client)
        self.__contacts = basecrm.services.ContactsService(self.http_client)
        self.__deals = basecrm.services.DealsService(self.http_client)
        self.__leads = basecrm.services.LeadsService(self.http_client)
        self.__loss_reasons = basecrm.services.LossReasonsService(self.http_client)
        self.__notes = basecrm.services.NotesService(self.http_client)
        self.__pipelines = basecrm.services.PipelinesService(self.http_client)
        self.__sources = basecrm.services.SourcesService(self.http_client)
        self.__stages = basecrm.services.StagesService(self.http_client)
        self.__tags = basecrm.services.TagsService(self.http_client)
        self.__tasks = basecrm.services.TasksService(self.http_client)
        self.__users = basecrm.services.UsersService(self.http_client)


    @property
    def accounts(self):
        return self.__accounts

    @property
    def associated_contacts(self):
        return self.__associated_contacts

    @property
    def contacts(self):
        return self.__contacts

    @property
    def deals(self):
        return self.__deals

    @property
    def leads(self):
        return self.__leads

    @property
    def loss_reasons(self):
        return self.__loss_reasons

    @property
    def notes(self):
        return self.__notes

    @property
    def pipelines(self):
        return self.__pipelines

    @property
    def sources(self):
        return self.__sources

    @property
    def stages(self):
        return self.__stages

    @property
    def tags(self):
        return self.__tags

    @property
    def tasks(self):
        return self.__tasks

    @property
    def users(self):
        return self.__users
