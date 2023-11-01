from datetime import datetime
import requests
from singer import get_logger

from tap_conversor.endpoints.endpoint import Endpoint

LOGGER = get_logger()
DEFAULT_CONNECTION_TIMEOUT = 300

class Last(Endpoint):
    def __init__(self, config) -> None:
        super().__init__(config)
    
    def sync(self, stream) -> list:
        session = requests.Session()
        parameter = self.config['currency']
        endpoint = f'/{stream}/{parameter}'
        endpoint_url = self.base_url + endpoint
        LOGGER.info("URL = " + endpoint_url)
        response = self.do_request(endpoint_url=endpoint_url,
                                   session=session)
        LOGGER.info(response.json)
        return response.json