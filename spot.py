from logging import getLogger
from typing import AnyStr
from network_wrappers import API_call

class PublicSpot():
    _log: getLogger
    base_endpoint: AnyStr

    def __init__(self):
        super(PublicSpot, self).__init__()

class PrivateSpot():
    _log: getLogger
    base_endpoint: AnyStr
    API_key: AnyStr

    def __init__(self):
        super(PrivateSpot, self).__init__()

        if not self.API_key:
            self._log.error('This method requires an API key !')
            return

    def my_open_orders(self,
                       max_retries: int = 1,
                       filter_pair: AnyStr = None):
        '''
        Will return ALL opened orders for an API key or just
         the opened orders for a certain trading pair.
        :param max_retries:
        :param filter_pair:
        :return:
        '''

        added_url = r'spot/open_orders'
        max_response_len = 50

        def return_data(offset):
            to_return = {'offset': offset,
                         'api_key': self.API_key}
            if filter_pair:
                to_return['filter_pair'] = filter_pair
            return to_return

        orders = []
        offset = 0

        while True:
            response = API_call(base_url=self.base_endpoint,
                                added_url=added_url,
                                data=return_data(offset),
                                max_retries=max_retries).send()
            if response['API_call_success']:
                if response['data']['success']:
                    current_orders = response['data']['orders']
                    orders += current_orders
                    if len(current_orders) >= max_response_len:

                        offset += max_response_len
                        self._log.info(f'Increased the offset to {offset}')

                    else:
                        response['data']['orders'] = orders
                        return response
                else:
                    return response
            else:
                return response

    def my_orders_history(self,
                          max_retries: int = 1,
                          filter_pair: AnyStr = None):
        '''
        Will return ALL the orders history for an API key or just
         the orders history for a certain trading pair.
        :param max_retries:
        :param filter_pair:
        :return:
        '''

        added_url = r'spot/orders_history'
        max_response_len = 50

        def return_data(offset):
            to_return = {'offset': offset,
                         'api_key': self.API_key}
            if filter_pair:
                to_return['filter_pair'] = filter_pair
            return to_return

        orders = []
        offset = 0

        while True:
            response = API_call(base_url=self.base_endpoint,
                                added_url=added_url,
                                data=return_data(offset),
                                max_retries=max_retries).send()
            if response['API_call_success']:
                if response['data']['success']:
                    current_orders = response['data']['orders']
                    orders += current_orders
                    if len(current_orders) >= max_response_len:

                        offset += max_response_len
                        self._log.info(f'Increased the offset to {offset}')

                    else:
                        response['data']['orders'] = orders
                        return response
                else:
                    return response
            else:
                return response