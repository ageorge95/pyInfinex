# pyInfinex
Python wrapper for the Infinex crypto exchange API

# How to use
- Some of the API endpoints are public, but some are private, meaning that you need an API key to access them - ex: posting a trading order, viewing your open orders ...

- To use the public API you do not need anything special, just run any public method from either spot, or wallet endpoints.

- To use the private API you first have to add a new entry in your user's path called "INFINEX_API_KEY" which must contain the API key created on infinex.cc

- All the available wrapper functions can be found in _EXAMPLE.py.

- Official API documentation: https://github.com/infinex-exchange/api-docs