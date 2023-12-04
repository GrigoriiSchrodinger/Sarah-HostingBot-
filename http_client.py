import requests

from utils import logger


class ClientHttp:
    @staticmethod
    def post(url, json):
        logger.logger.info(f"requests\nPOST - {url}\n json - {json}")
        try:
            return requests.post(url, json)
        except Exception as error:
            logger.logger.warning(error)
            return requests.RequestException
