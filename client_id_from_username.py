from base_client import BaseClient
import requests
from exception import HandlerException



class ClientIdFromUsername(BaseClient):
    method = 'users.get'

    http_method = 'GET'

    def __init__(self, user_id, fields=None, name_case=None):
        self.user_id = user_id
        self.fields = fields
        self.name_case = name_case
        self.params = {}
        self.real_id = None

    def get_params(self):
        self.params['user_ids'] = self.user_id
        if self.fields is not None:
            self.params['fields'] = self.fields
        if self.name_case is not None:
            self.params['name_case'] = self.name_case
        return self.params

    def _get_data(self, method, http_method):
        response = requests.get(self.generate_url(method), self.get_params())
        print(response.url)

        return self.response_handler(response)

    def response_handler(self, response):
        if response.status_code != 200:
            raise HandlerException('response in ClientIdFromUsername with not 200 status')
        else:
            self.real_id = response.json()['response'][0]['uid']
