from basecrm.configuration import Configuration
from basecrm.http_client import HttpClient

import basecrm.services
import basecrm.sync


class Client(object):
    """
    The :class:`Client <Client>` is the entry point to all services and actions.

    :attribute :class:`Configuration <basecrm.Configuration>` config: Current Base CRM client configuration.
    :attribute :class:`HttpClient <basecrm.HttpClient>` http_client: Http client.

    :copyright: (c) 2016 by BaseCRM developers (developers@getbase.com).
    :license: MIT, see LICENSE for more details.
    """

    def __init__(self, **options):
        """
        Usage::

          >>> import os
          >>> import basecrm
          >>> client = basecrm.Client(access_token=os.environ.get('BASECRM_ACCESS_TOKEN'))
          <basecrm.Client>


        :param str access_token: Personal access token.
        :param str base_url: (optional) Base url for the api. Default: ``https://api.getbase.com``.
        :param str user_agent: (optional) Client user agent. Default: ``BaseCRM/v2 Python/{basecrm.VERSION}``.
        :param bool verbose: (optional) Verbose/debug mode. Default: ``False``.
        :param int timeout: (optional) Connection and response timeout. Default: **30** seconds.
        :param bool verify_ssl: (optional) Whether to verify ssl or not. Default: ``True``.

        :raises ConfigurationError: if no ``access_token`` provided.
        :raises ConfigurationError: if provided ``access_token`` is invalid - contains disallowed characters.
        :raises ConfigurationError: if provided ``access_token`` is invalid - has invalid length.
        :raises ConfigurationError: if provided ``base_url`` is invalid.
        """

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

        self.__sync = basecrm.sync.SyncService(self.http_client)

    @property
    def accounts(self):
        """
        :return: :class:`AccountsService <basecrm.AccountsService>` object that gives you an access to all Account related actions.
        :rtype: basecrm.AccountsService
        """
        return self.__accounts

    @property
    def associated_contacts(self):
        """
        :return: :class:`AssociatedContactsService <basecrm.AssociatedContactsService>` object that gives you an access to all AssociatedContact related actions.
        :rtype: basecrm.AssociatedContactsService
        """
        return self.__associated_contacts

    @property
    def contacts(self):
        """
        :return: :class:`ContactsService <basecrm.ContactsService>` object that gives you an access to all Contact related actions.
        :rtype: basecrm.ContactsService
        """
        return self.__contacts

    @property
    def deals(self):
        """
        :return: :class:`DealsService <basecrm.DealsService>` object that gives you an access to all Deal related actions.
        :rtype: basecrm.DealsService
        """
        return self.__deals

    @property
    def leads(self):
        """
        :return: :class:`LeadsService <basecrm.LeadsService>` object that gives you an access to all Lead related actions.
        :rtype: basecrm.LeadsService
        """
        return self.__leads

    @property
    def loss_reasons(self):
        """
        :return: :class:`LossReasonsService <basecrm.LossReasonsService>` object that gives you an access to all LossReason related actions.
        :rtype: basecrm.LossReasonsService
        """
        return self.__loss_reasons

    @property
    def notes(self):
        """
        :return: :class:`NotesService <basecrm.NotesService>` object that gives you an access to all Note related actions.
        :rtype: basecrm.NotesService
        """
        return self.__notes

    @property
    def pipelines(self):
        """
        :return: :class:`PipelinesService <basecrm.PipelinesService>` object that gives you an access to all Pipeline related actions.
        :rtype: basecrm.PipelinesService
        """
        return self.__pipelines

    @property
    def sources(self):
        """
        :return: :class:`SourcesService <basecrm.SourcesService>` object that gives you an access to all Source related actions.
        :rtype: basecrm.SourcesService
        """
        return self.__sources

    @property
    def stages(self):
        """
        :return: :class:`StagesService <basecrm.StagesService>` object that gives you an access to all Stage related actions.
        :rtype: basecrm.StagesService
        """
        return self.__stages

    @property
    def tags(self):
        """
        :return: :class:`TagsService <basecrm.TagsService>` object that gives you an access to all Tag related actions.
        :rtype: basecrm.TagsService
        """
        return self.__tags

    @property
    def tasks(self):
        """
        :return: :class:`TasksService <basecrm.TasksService>` object that gives you an access to all Task related actions.
        :rtype: basecrm.TasksService
        """
        return self.__tasks

    @property
    def users(self):
        """
        :return: :class:`UsersService <basecrm.UsersService>` object that gives you an access to all User related actions.
        :rtype: basecrm.UsersService
        """
        return self.__users

    @property
    def sync(self):
        """
        :return: :class:`SyncService <basecrm.SyncService>` object that gives you an access to all low-level Sync API  related actions.
        :rtype: basecrm.SyncService
        """
        return self.__sync
