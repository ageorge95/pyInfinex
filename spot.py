from logging import getLogger
from typing import AnyStr
from network_wrappers import API_call
from utils import check_API_key

class PublicSpot():
    _log: getLogger
    base_endpoint: AnyStr

    def __init__(self):
        super(PublicSpot, self).__init__()

    def aggregated_order_book(self,
                              pair,
                              max_retries: int = 1,):

        added_url = r'spot/orderbook'

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data={'pair': pair},
                        max_retries=max_retries).send()

class PrivateSpot():
    _log: getLogger
    base_endpoint: AnyStr
    API_key: AnyStr

    def __init__(self):
        super(PrivateSpot, self).__init__()

    @check_API_key
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

    @check_API_key
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

    @check_API_key
    def post_new_order(self,
                       pair: AnyStr,
                       side: AnyStr,
                       type: AnyStr,
                       price: AnyStr = None,
                       amount: AnyStr = None,
                       total: AnyStr = None,
                       time_in_force: AnyStr = 'GTC',
                       max_retries: int = 1):

        added_url = r'spot/open_orders/new'

        def return_data():
            to_return = {'api_key': self.API_key,
                         'pair': pair,
                         'side': side,
                         'type': type,
                         'time_in_force': time_in_force}
            # some sanity checks
            if price and type == 'MARKET':
                self._log.error(f"You specified a price and a MARKET type order. That does not make sense."
                                f" Please review the call parameters.")
                return {'API_call_success': False,
                        'data': None}

            if total and amount:
                self._log.error(f"You specified both a total and an amount. That does not make sense."
                                f" Please review the call parameters.")
                return {'API_call_success': False,
                        'data': None}

            if price and type in ['LIMIT', 'STOP_LIMIT']:
                to_return['price'] = price

            if total:
                to_return['total'] = total

            if amount:
                to_return['amount'] = amount

            return to_return

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=return_data(),
                        max_retries=max_retries).send()

    @check_API_key
    def match_order_open(self,
                                pair: AnyStr,
                                side: AnyStr,
                                type: AnyStr,
                                amount: AnyStr,
                                price: AnyStr):

        my_open_orders_response = self.my_open_orders(filter_pair = pair)
        if my_open_orders_response['API_call_success']:
            if my_open_orders_response['data']['success']:
                current_order_matches = list(filter(lambda _:_['side'] == side
                                                             and _['type'] == type
                                                             and _['amount'] == amount
                                                             and _['price'] == price,
                                                    my_open_orders_response['data']['orders']))
                # return the matched order
                if len(current_order_matches):
                    return {'API_call_success': True,
                            'data': current_order_matches[0]}

        # the order could not be matched, return an empty dict
        return {'API_call_success': False,
                'data': {}}

    @check_API_key
    def match_order_closed(self,
                           pair: AnyStr,
                           side: AnyStr,
                           type: AnyStr,
                           amount: AnyStr,
                           price: AnyStr):

        my_order_history_response = self.my_orders_history(filter_pair = pair)
        if my_order_history_response['API_call_success']:
            if my_order_history_response['data']['success']:
                current_order_matches = list(filter(lambda _:_['side'] == side
                                                             and _['type'] == type
                                                             and _['amount'] == amount
                                                             and _['price'] == price,
                                                    my_order_history_response['data']['orders']))
                # return the matched order
                if len(current_order_matches):
                    return {'API_call_success': True,
                            'data': current_order_matches[0]}

        # the order could not be matched, return an empty dict
        return {'API_call_success': False,
                'data': {}}

    @check_API_key
    def match_order_all(self,
                        pair: AnyStr,
                        side: AnyStr,
                        type: AnyStr,
                        amount: AnyStr,
                        price: AnyStr):
        # first double check the order in my_open_orders
        my_open_orders_response = self.match_order_open(pair = pair,
                                                          side = side,
                                                          type = type,
                                                          amount = amount,
                                                          price = price)
        if my_open_orders_response['API_call_success']:
            return my_open_orders_response

        # if nothing was found then double check in the order history, perhaps the order was executed instantly
        my_order_history_response = self.match_order_closed(pair = pair,
                                                          side = side,
                                                          type = type,
                                                          amount = amount,
                                                          price = price)
        if my_order_history_response['API_call_success']:
            return my_order_history_response

        # otherwise the order could not be matched, return an empty dict
        return {'API_call_success': False,
                'data': {}}

    @check_API_key
    def cancel_order(self,
                     obid: int,
                     max_retries: int = 1):
        '''
        Will cancel an order based on the order ID
        :param obid:
        :param max_retries:
        :return:
        '''

        added_url = r'spot/open_orders/cancel'

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data={'api_key': self.API_key,
                              'obid': obid},
                        max_retries=max_retries).send()