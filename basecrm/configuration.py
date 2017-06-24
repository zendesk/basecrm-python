import re

from basecrm.version import VERSION
from basecrm.errors import ConfigurationError


class Configuration(object):
    """Base CRM client configuration :class:`Configuration <Configuration>` object.

    Used by :class:`HttpClient <HttpClient>` to send requests to Base CRM's servers.
    """

    URL_REGEXP = r'\b(?:(?:https?|http):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]'

    def __init__(self, **options):
        """
        :param str access_token: Personal access token.
        :param str base_url: (optional) Base url for the api. Default: ``https://api.getbase.com``.
        :param str user_agent: (optional) Client user agent. Default: ``BaseCRM/v2 Python/{basecrm.VERSION}``.
        :param bool verbose: (optional) Verbose/debug mode. Default: ``False``.
        :param int timeout: (optional) Connection and response timeout. Default: **30** seconds.
        :param bool verify_ssl: (optional) Whether to verify ssl or not. Default: ``True``.
        """

        self.access_token = options.get('access_token')
        self.base_url = options['base_url'] if 'base_url' in options else 'https://api.getbase.com'
        self.user_agent = options['user_agent'] if 'user_agent' in options else 'BaseCRM/v2 Python/{0}'.format(VERSION)
        self.verbose = options['verbose'] if 'verbose' in options else False
        self.timeout = options['timeout'] if 'timeout' in options else 30
        self.verify_ssl = options['verify_ssl'] if 'verify_ssl' in options else True

        if self.verbose:
            print("BaseCRM client configuration: ") + str(self.__dict__)

    def validate(self):
        """Validates whether a configuration is valid.

        :rtype: bool
        :raises ConfigurationError: if no ``access_token`` provided.
        :raises ConfigurationError: if provided ``access_token`` is invalid - contains disallowed characters.
        :raises ConfigurationError: if provided ``access_token`` is invalid - has invalid length.
        :raises ConfigurationError: if provided ``base_url`` is invalid.
        """
        if self.access_token is None:
            raise ConfigurationError('No access token provided. '
                                     'Set your access token during client initialization using: '
                                     '"basecrm.Client(access_token= <YOUR_PERSONAL_ACCESS_TOKEN>)"')

        if re.search(r'\s', self.access_token):
            raise ConfigurationError('Provided access token is invalid '
                                     'as it contains disallowed characters. '
                                     'Please double-check you access token.')

        if len(self.access_token) != 64:
            raise ConfigurationError('Provided access token is invalid '
                                     'as it has invalid length. '
                                     'Please double-check your access token.')

        if not self.base_url or not re.match(self.URL_REGEXP, self.base_url):
            raise ConfigurationError('Provided base url is invalid '
                                     'as it not a valid URI. '
                                     'Please make sure it incldues the schema part, '
                                     'both http and https are accepted, '
                                     'and the hierarchical part')

        return True
