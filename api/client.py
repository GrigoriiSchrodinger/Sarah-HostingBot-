import requests

from utils.logger import logger


class APIConfig:
    BASE_URL = "https://api.ishosting.com/"


class ClientHttp:
    def __init__(self):
        self.base_url = APIConfig.BASE_URL

    def _send_request(
            self,
            endpoint: str,
            method: str = 'GET',
            data: dict = None,
            headers: dict = None,
            params: dict = None
    ):
        url = f"{self.base_url}{endpoint}"
        response = None
        try:
            logger.info(f"requests - {method} endpoint - {url} data - {data}")
            if method == 'GET':
                response = requests.get(url, headers=headers, params=params)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, params=params)
            return response.json()
        except Exception as error:
            logger.warning(error)
            return requests.RequestException
