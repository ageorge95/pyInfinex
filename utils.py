from decimal import Decimal
from typing import AnyStr

def check_API_key(func):
    def inner(*args, **kwargs):
        if not args[0].API_key:
            args[0]._log.error(f'{func.__name__} requires an API key !')
        return func(*args, **kwargs)
    return inner

def normalize_Decimal(nr) -> AnyStr:
    nr = Decimal(nr)
    exponent = abs(nr.as_tuple().exponent)
    if exponent:
        nr = nr.normalize()

    # the exponent may change after normalize
    exponent = abs(nr.as_tuple().exponent)

    return f'{nr:.{exponent}f}'