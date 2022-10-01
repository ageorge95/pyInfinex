from logging import getLogger
from typing import AnyStr
from wallet import PublicWallet,\
    PrivateWallet
from spot import PublicSpot,\
    PrivateSpot

class pyVayamos(PublicWallet,
                PrivateWallet,
                PublicSpot,
                PrivateSpot):

    def __init__(self,
                 API_key: AnyStr = None,
                 base_endpoint: AnyStr = 'https://api.vayamos.cc'):

        self._log = getLogger()
        self.API_key = API_key
        self.base_endpoint = base_endpoint

        super(pyVayamos, self).__init__()

