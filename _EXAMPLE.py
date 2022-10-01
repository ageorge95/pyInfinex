from logger import configure_logger
from pyVayamos import pyVayamos

if __name__ == '__main__':
    configure_logger()
    # public wallet examples
    API_obj = pyVayamos()

    # print(API_obj.assets_list())