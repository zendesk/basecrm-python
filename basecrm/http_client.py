import requests
import json


from bunch import bunchify

from basecrm.errors import RateLimitError, RequestError, ResourceError, ServerError


class HttpClient(object):
    API_VERSION = '/v2'

    def __init__(self, config):
        self.config = config
        if self.config.verbose:
            self.enable_logging()

    def get(self, url, params=None, **kwargs):
        return self.request('get', url, params=params, **kwargs)

    def post(self, url, body=None, **kwargs):
        return self.request('post', url, body=body, **kwargs)

    def put(self, url, body=None, **kwargs):
        return self.request('put', url, body=body, **kwargs)

    def delete(self, url, params=None, **kwargs):
        return self.request('delete', url, params=params, **kwargs)

    def request(self, method, url, params=None, body=None, **kwargs):
        url = "{base_url}{version}{resource}".format(base_url=self.config.base_url,
                                                     version=self.API_VERSION,
                                                     resource=url)
        headers = {
            'Accept': 'application/json',
            'Authorization': "Bearer {0}".format(self.config.access_token)
        }

        if body is not None:
            headers['Content-Type'] = 'application/json'
            body = json.dumps(self.wrap_envelope(body))

        resp = requests.request(method, url,
                                params=params,
                                data=body,
                                headers=headers,
                                timeout=float(self.config.timeout),
                                verify=self.config.verify_ssl)

        if not (200 <= resp.status_code < 300):
            self.handle_error_response(resp)

        if 'Content-Type' in resp.headers and 'json' in resp.headers['Content-Type']:
            resp_body = self.unwrap_envelope(resp.json())
        else:
            resp_body = resp.content

        return (resp.status_code, resp.headers, resp_body)

    def handle_error_response(self, resp):
        try:
            errors = resp.json()
        except:
            raise Exception('Unknown HTTP error response. Json expected. '
                            'HTTP response code={0}. '
                            'HTTP response body={1}'.format(resp.status_code,
                                                            resp.text))
        resp_code = resp.status_code
        if resp_code == 422:
            raise ResourceError(resp_code, errors)
        elif resp_code == 429:
            raise RateLimitError()
        elif 400 <= resp_code < 500:
            raise RequestError(resp_code, errors)
        elif 500 <= resp_code < 600:
            raise ServerError(resp_code, errors)
        else:
            raise Exception('Unknown HTTP error response')

    @staticmethod
    def wrap_envelope(body):
        return {'data': body}

    @staticmethod
    def unwrap_envelope(body):
        return [bunchify(item['data']) for item in body['items']] if 'items' in body else bunchify(body['data'])

    def enable_logging(self):
        import logging
        try:
            import http.client as http_client
        except ImportError:
            # Python 2
            import httplib as http_client
        http_client.HTTPConnection.debuglevel = 1

        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True
