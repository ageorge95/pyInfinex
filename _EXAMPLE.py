from logger import configure_logger
from os import getenv
from pyVayamos import pyVayamos

if __name__ == '__main__':
    configure_logger()
    # public wallet examples
    # API_obj = pyVayamos()
    # print(API_obj.assets_list())

    # public spot examples
    # TBD

    # private wallet examples
    # TBD

    # private spot examples
    API_obj = pyVayamos(getenv('VAYAMOS_API_KEY'))
    API_obj.my_open_orders()