def check_API_key(func):
    def inner(*args, **kwargs):
        if not args[0].API_key:
            args[0]._log.error(f'{func.__name__} requires an API key !')
        return func(*args, **kwargs)
    return inner