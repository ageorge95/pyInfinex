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

    # get all the DEPOSIT transactions
    # pprint(API_obj.wallet_transactions(type='DEPOSIT'))

    # get all the DEPOSIT transactions for a certain asset
    # pprint(API_obj.wallet_transactions(type='DEPOSIT',
    #                                    asset='XSHIB'))
    # pprint(API_obj.wallet_transactions(type='WITHDRAWAL',
    #                                    asset='XSHIB'))

    # ########### private spot examples ###########
    # initialize the APi wrapper
    # API_obj = pyVayamos(getenv('VAYAMOS_API_KEY'))

    # return all open orders
    # pprint(API_obj.my_open_orders())

    # return open orders for just 1 pair
    # pprint(API_obj.my_open_orders(filter_pair='BPX/USDT'))

    # return the full orders history
    # pprint(API_obj.my_orders_history())

    # return the filtered orders history
    # pprint(API_obj.my_orders_history(filter_pair='BPX/USDT'))

    # post a SELL order for 1030BPX at 0.00049USDT per BPX
    # pprint(API_obj.post_new_order(pair='BPX/USDT',
    #                               side='SELL',
    #                               type='LIMIT',
    #                               amount='1030',
    #                               price='0.00049'))

    # cancel an order based on the order ID
    # pprint(API_obj.cancel_order(obid=29033))

    # get the data for an open order, check in both open and closed (canceled or filled) orders
    # pprint(API_obj.match_order_all(pair='BPX/USDT',
    #                                side='SELL',
    #                                type='LIMIT',
    #                                amount='1030',
    #                                price='0.00049'))

    # get the data for an open order, check only in the open orders
    # pprint(API_obj.match_order_open(pair='BPX/USDT',
    #                                 side='SELL',
    #                                 type='LIMIT',
    #                                 amount='1030',
    #                                 price='0.00049'))

    # get the data for an open order, check only in the closed (canceled or filled) orders
    # pprint(API_obj.match_order_closed(pair='TAD/USDT',
    #                                   side='BUY',
    #                                   type='LIMIT',
    #                                   amount='587.55',
    #                                   price='0.000851',
    #                                   starting_offset=0,
    #                                   max_offset = 50))