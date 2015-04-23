import re

from basecrm.version import VERSION
from basecrm.errors import ConfigurationError


class Configuration(object):
    URL_REGEXP = r'\b(?:(?:https?|http):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]'

    def __init__(self, **options):
        self.access_token = options.get('access_token')
        self.base_url = options['base_url'] if 'base_url' in options else 'https://api.getbase.com'
        self.user_agent = options['user_agent'] if 'user_agent' in options else 'BaseCRM/v2 Python/{0}'.format(VERSION)
        self.verbose = options['verbose'] if 'verbose' in options else False
        self.timeout = options['timeout'] if 'timeout' in options else 30
        self.verify_ssl = options['verify_ssl'] if 'verify_ssl' in options else True

        if self.verbose:
            print "BaseCRM client configuration: " + str(self.__dict__)

    def validate(self):
        if self.access_token is None:
            raise ConfigurationError('No access token provided. '
                                     'Set your access token during client initialization using: '
                                     '"basecrm.Client(access_token= <YOUR_PERSONAL_ACCESS_TOKEN>)"')

        if re.search(r'\s', self.access_token):
            raise ConfigurationError('Pvoided access token is invalid '
                                     'as it contains disallowed characters. '
                                     'Please double-check you access token.')

        if len(self.access_token) != 64:
            raise ConfigurationError('Provieded access token is invalid '
                                     'as it has invalid length. '
                                     'Please double-check your access token.')

        if not self.base_url or not re.match(self.URL_REGEXP, self.base_url):
            raise ConfigurationError('Provided base url is invalid '
                                     'as it not a valid URI. '
                                     'Please make sure it incldues the schema part, '
                                     'both http and https are accepted, '
                                     'and the hierarchical part')

        return True
