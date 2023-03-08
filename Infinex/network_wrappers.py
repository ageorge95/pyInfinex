from requests import get
from typing import AnyStr,\
    Dict
from logging import getLogger
from traceback import format_exc

class API_call():
    def __init__(self,
                 base_url: AnyStr,
                 added_url: AnyStr,
                 data: Dict,
                 max_retries: int = 1):

        self._log = getLogger()
        self.final_URL = base_url + '/' + added_url
        self.max_retries = max_retries
        self.data = data

    def send(self) -> Dict:

        current_retry = 0
        while current_retry < self.max_retries:
            try:
                self._log.info(f'Sending an API call to {self.final_URL} at retry attempt {current_retry + 1}/{self.max_retries}')
                return {'API_call_success': True,
                        'data': get(self.final_URL,
                                    json=self.data,
                                    timeout=(5,5)).json()}
            except:
                self._log.error(f'Failed to send an API call to {self.final_URL} at retry attempt {current_retry + 1}/{self.max_retries}')
                current_retry += 1
                self._log.error(format_exc(chain=False))

        return {'API_call_success': False,
                'data': None}
