from logging import getLogger
from typing import AnyStr

class PublicSpot():
    _log: getLogger
    base_endpoint: AnyStr

    def __init__(self):
        super(PublicSpot, self).__init__()

class PrivateSpot():
    _log: getLogger
    base_endpoint: AnyStr

    def __init__(self):
        super(PrivateSpot, self).__init__()