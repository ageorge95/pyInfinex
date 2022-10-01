from logging import getLogger
from typing import AnyStr
from .network_wrappers import API_call

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