from logger import configure_logger
from os import getenv
from pyVayamos import pyVayamos

if __name__ == '__main__':
    configure_logger()
    # # public wallet examples
    # # initialize the APi wrapper
    # API_obj = pyVayamos()
    # # get a list of all assets
    # print(API_obj.assets_list())

    # public spot examples
    # TBD

    # private wallet examples
    # TBD

    # private spot examples
    # initialize the APi wrapper
    API_obj = pyVayamos(getenv('VAYAMOS_API_KEY'))
    # return all open orders
    print(API_obj.my_open_orders())
    # return open orders for just 1 pair
    print(API_obj.my_open_orders(filter_pair='BPX/USDT'))