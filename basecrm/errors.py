from bunch import bunchify


class ConfigurationError(Exception):
    pass


class RateLimitError(Exception):
    pass


class BaseError(Exception):
    def __init__(self, http_status, errors_payload):
        self.http_status = http_status
        self.errors = [bunchify(error_envelope['error'])
                       for error_envelope in errors_payload['errors']]
        self.logref = errors_payload['meta']['logref']

        message = "\n".join([str(error) for error in self.errors])
        super(BaseError, self).__init__(message)


class RequestError(BaseError):
    pass


class ResourceError(BaseError):
    pass


class ServerError(BaseError):
    pass
