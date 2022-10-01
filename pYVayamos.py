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
                 API_key: AnyStr = None):

        self._log = getLogger()
        self.API_key = API_key

        super(pyVayamos, self).__init__()

    