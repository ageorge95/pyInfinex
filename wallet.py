from logging import getLogger
from typing import AnyStr

class PublicWallet():
    _log: getLogger
    base_endpoint: AnyStr

    def __init__(self):
        super(PublicWallet, self).__init__()

class PrivateWallet():
    _log: getLogger
    base_endpoint: AnyStr

    def __init__(self):
        super(PrivateWallet, self).__init__()