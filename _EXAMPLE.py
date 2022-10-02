from logger import configure_logger
from os import getenv
from pprint import pprint
from pyVayamos import pyVayamos

if __name__ == '__main__':
    configure_logger()
    # ########### public wallet examples ###########
    # initialize the APi wrapper
    # API_obj = pyVayamos()

    # get a list of all assets
    # pprint(API_obj.assets_list())

    # ########### public spot examples ###########
    # aggregated order book for BPX/USDT
    # pprint(API_obj.aggregated_order_book(pair='BPX/USDT'))

    # ########### private wallet examples ###########
    # initialize the APi wrapper
    # API_obj = pyVayamos(getenv('VAYAMOS_API_KEY'))

    # get all the balances
    # pprint(API_obj.wallet_balances())

    # get a certain asset balance
    # pprint(API_obj.wallet_balances(search='BPX'))

    # ########### private spot examples ###########
    # initialize the APi wrapper
    # API_obj = pyVayamos(getenv('VAYAMOS_API_KEY'))

    # return all open orders
    # pprint(API_obj.my_open_orders())

    # return open orders for just 1 pair
    # pprint(API_obj.my_open_orders(filter_pair='BPX/USDT'))

    # return the full orders history
    # pprint(API_obj.my_orders_history())

    # post a SELL order for 1030BPX at 0.00049USDT per BPX
    # pprint(API_obj.post_new_order(pair='BPX/USDT',
    #                               side='SELL',
    #                               type='LIMIT',
    #                               amount='1030',
    #                               price='0.00049'))

    # cancel an order based on the order ID
    # pprint(API_obj.cancel_order(obid=27863))