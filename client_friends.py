from base_client import BaseClient
import requests
from datetime import datetime


class ClientFriends(BaseClient):
    method = 'friends.get'

    http_method = 'GET'

    def __init__(self,
                 user_id,
                 order='random',
                 list_id=None,
                 count=None,
                 offset=None,
                 fields='bdate',
                 name_case=None):
        self.user_id = user_id
        self.order = order
        self.list_id = list_id
        self.count = count
        self.offset = offset
        self.fields = fields
        self.name_case = name_case
        self.params = {}
        self.ages_list = None

    def _get_data(self, method, http_method):

        response = requests.get(self.generate_url(method), self.get_params())

        return self.response_handler(response)

    def get_params(self):
        self.params['user_id'] = self.user_id
        self.params['order'] = self.order
        if self.list_id is not None:
            self.params['list_id'] = self.list_id
        if self.count is not None:
            self.params['count'] = self.count
        if self.offset is not None:
            self.params['offset'] = self.offset
        self.params['fields'] = self.fields
        if self.name_case is not None:
            self.params['name_case'] = self.name_case
        return self.params

    def response_handler(self, response):
        if response.status_code != 200:
            print('Error!') # todo raise an exception
        else:
            response_dict = response.json()
            self.ages_list = []

            for elem in response_dict.get('response'):
                try:
                    bdate = datetime.strptime(elem['bdate'], '%d.%m.%Y')
                    self.ages_list.append((datetime.today() - bdate).days // 365)
                except ValueError:
                    continue
                except KeyError:
                    continue
                except Exception:
                    print(Exception)
                    continue
