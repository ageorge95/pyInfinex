from logging import getLogger
from typing import AnyStr,\
    List
from Infinex.network_wrappers import API_call
from Infinex.utils import check_API_key

class PublicWallet():
    _log: getLogger
    base_endpoint: AnyStr

    def __init__(self):
        super(PublicWallet, self).__init__()

    def assets_list(self,
                    max_retries: int = 1):
        '''
        Will return all the assets trading on the exchange;
         Takes into account the 50 elements length limit.
        :param max_retries:
        :return:
        '''

        added_url = r'wallet/assets'
        max_response_len = 50

        assets = {}
        offset = 0

        while True:
            response = API_call(base_url=self.base_endpoint,
                                added_url=added_url,
                                data={'offset': offset},
                                max_retries=max_retries).send()
            if response['API_call_success']:
                if response['data']['success']:
                    current_assets = response['data']['assets']
                    assets.update(current_assets)
                    if len(current_assets) >= max_response_len:

                        offset += max_response_len
                        self._log.info(f'Increased the offset to {offset}')

                    else:
                        response['data']['assets'] = assets
                        return response
                else:
                    return response
            else:
                return response

class PrivateWallet():
    _log: getLogger
    base_endpoint: AnyStr
    API_key: AnyStr

    def __init__(self):
        super(PrivateWallet, self).__init__()

    @check_API_key
    def wallet_transactions(self,
                            asset: AnyStr = None,
                            type: AnyStr = None,
                            status: AnyStr = None,
                            max_retries: int = 1):
        added_url = r'wallet/transactions'
        max_response_len = 50

        transactions = []
        offset = 0

        def return_data(offset):
            to_return = {'offset': offset,
                         'api_key': self.API_key}
            if asset:
                to_return['asset'] = asset
            if type:
                to_return['type'] = type
            if status:
                to_return['status'] = status
            return to_return

        while True:
            response = API_call(base_url=self.base_endpoint,
                                added_url=added_url,
                                data=return_data(offset),
                                max_retries=max_retries).send()
            if response['API_call_success']:
                if response['data']['success']:
                    current_transactions = response['data']['transactions']
                    transactions += current_transactions
                    if len(current_transactions) >= max_response_len:

                        offset += max_response_len
                        self._log.info(f'Increased the offset to {offset}')

                    else:
                        response['data']['transactions'] = transactions
                        return response
                else:
                    return response
            else:
                return response

    @check_API_key
    def wallet_balances(self,
                        symbols: List = None,
                        max_retries: int = 1):
        '''
        Will return all the assets trading on the exchange;
         Takes into account the 50 elements length limit.
        :param symbols:
        :param max_retries:
        :return:
        '''

        added_url = r'wallet/balances'
        max_response_len = 50

        balances = {}
        offset = 0

        def return_data(offset):
            to_return = {'api_key': self.API_key}

            if symbols:
                to_return['symbols'] = symbols
            else:
                # symbols and offset cannot be used at the same time
                to_return['offset'] = offset
            return to_return

        while True:
            response = API_call(base_url=self.base_endpoint,
                                added_url=added_url,
                                data=return_data(offset),
                                max_retries=max_retries).send()
            if response['API_call_success']:
                if response['data']['success']:
                    current_balances = response['data']['balances']
                    balances.update(current_balances)
                    if len(current_balances) >= max_response_len:

                        offset += max_response_len
                        self._log.info(f'Increased the offset to {offset}')

                    else:
                        response['data']['balances'] = balances
                        return response
                else:
                    return response
            else:
                return response