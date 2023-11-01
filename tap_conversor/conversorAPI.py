from typing import Dict, List

from singer.logger import get_logger
from tap_conversor.endpoints.last import Last
from tap_conversor.endpoints.daily import Daily
from tap_conversor.endpoints.endpoint import Endpoint

LOGGER = get_logger()
DEFAULT_CONNECTION_TIMEOUT = 30


class ConversorAPI(Endpoint):
    def __init__(self, config: Dict) -> None:
        self.config = config

    def sync(self, stream: str) -> List:
        if stream == "last":
            data = Last(self.config).sync(stream)
        elif stream == 'daily':
            data = Daily(self.config).sync(stream)
        else:
            raise ValueError(f"Unrecognized stream: {stream}")

        return data