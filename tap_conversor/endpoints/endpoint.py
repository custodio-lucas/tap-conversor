from typing import Dict, List
import os

from singer.logger import get_logger
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from datetime import datetime, timedelta
import singer
from abc import ABC

LOGGER = get_logger()
DEFAULT_CONNECTION_TIMEOUT = 300


class Endpoint(ABC):

    def __init__(self, config) -> None:
        self.base_url = "https://economia.awesomeapi.com.br/json"
        self.config = config
        self.headers = {}

    def do_request(
        self,
        endpoint_url,
        session: requests.Session
    ) -> requests.Response:

        response = self.requests_retry_session(session=session).get(
            endpoint_url,
            headers=self.headers,
            auth=None,
            params=None,
            timeout=DEFAULT_CONNECTION_TIMEOUT,
        )

        return response

    def get_data(self, params) -> List:
        session = requests.Session()
        
        response = self.do_request(params=params, session=session)

        if type(response) is list:
            for record in response:
                record['extracted_at'] = str(datetime.now())

        return response

    def requests_retry_session(
        self,
        retries=5,
        backoff_factor=2,
        status_forcelist=(500, 502, 504),
        session=None,
    ):
        session = session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
            raise_on_status=False,
        )

        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session