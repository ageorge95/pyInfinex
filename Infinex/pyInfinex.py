from logging import getLogger
from typing import AnyStr
from Infinex.wallet import PublicWallet,\
    PrivateWallet
from Infinex.spot import PublicSpot,\
    PrivateSpot

base_endpoint: AnyStr = 'https://api.infinex.cc'

class pyInfinex(PublicWallet,
                PrivateWallet,
                PublicSpot,
                PrivateSpot):

    def __init__(self,
                 API_key: AnyStr = None):

        self._log = getLogger()
        self.API_key = API_key

        self.base_endpoint = base_endpoint

        super(pyInfinex, self).__init__()

