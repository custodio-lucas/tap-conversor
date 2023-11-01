from datetime import datetime
import requests
from singer import get_logger

from tap_conversor.endpoints.endpoint import Endpoint

LOGGER = get_logger()
DEFAULT_CONNECTION_TIMEOUT = 300


class Daily(Endpoint):
    def __init__(self, config) -> None:
        super().__init__(config)
    
    def sync(self, stream) -> list:
        session = requests.Session()
        params = self.config
        interval = self.number_of_days()
        endpoint = f'/{stream}/{params["currency"]}/{interval}'
        endpoint_url = self.base_url + endpoint
        LOGGER.info("URL = " + endpoint_url)
        response = self.do_request(endpoint_url=endpoint_url,
                                   session=session)
        return response.json
    
    def number_of_days(self):
        start_date = datetime.strptime(self.config["start_date"], r"%Y%m%d")
        end_date = datetime.strptime(self.config["end_date"], r"%Y%m%d")

        days_between = end_date - start_date
        return days_between.days