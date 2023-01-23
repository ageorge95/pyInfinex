from decimal import Decimal
from typing import AnyStr

def check_API_key(func):
    def inner(*args, **kwargs):
        if not args[0].API_key:
            args[0]._log.error(f'{func.__name__} requires an API key !')
        return func(*args, **kwargs)
    return inner

def full_nr_normalisation(nr: [Decimal, str, int, float]) -> AnyStr:

    # first remove any trailing of 0 from the nr
    # nr must first be converted to a Decimal, to correctly display it
    if type(nr) != type(Decimal):
        nr = Decimal(str(nr))

    nr_decimal_places = abs(nr.as_tuple().exponent)
    nr = f'{nr:.{nr_decimal_places}f}'

    # now remove all trailing 0s
    while nr.endswith('0') and len(nr) > 1 and ',' in nr:
        nr = nr[:-1]

    # then convert the number to a decimal
    nr = Decimal(str(nr))

    # and finally return it
    nr_decimal_places = abs(nr.as_tuple().exponent)
    return f'{nr:.{nr_decimal_places}f}'