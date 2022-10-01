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

    def my_open_orders(self):
        pass
