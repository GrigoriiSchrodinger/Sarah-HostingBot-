from datetime import datetime
from api.client import ClientHttp
from utils.config import cache, db
from utils.logger import logger


class APIHosting(ClientHttp):
    def auth(self, user_id: str) -> str:
        """
        Authenticate the user and retrieve a token.

        Args:
            user_id (str): The user ID.

        Returns:
            str: The authentication token.
        """
        token_user = cache.get(user_id)
        if token_user is None:
            user_date = db.get_user_data(id_user="275293218")
            try:
                auth_data = {
                    "type": "password",
                    "email": user_date["email"],
                    "password": user_date["password"],
                }
                token = self._send_request(endpoint="auth/token", method="POST", data=auth_data).get("token")
                if token is None:
                    logger.warning("Token not found in response")
                    raise ValueError("Token not found in response")
                cache[user_id] = token
                return token
            except Exception as error:
                logger.warning(error)
                raise error
        else:
            return token_user

    def vpn_list(self, user_id: str) -> list:
        """
          Retrieves a list of VPN details for a given user.

          This function fetches details of all VPNs associated with the provided user ID.
          It makes a request to the 'vpn/list' endpoint and processes the response to
          format the VPN details in a readable manner.

          Args:
              user_id (str): The user ID for which VPN details are to be retrieved.

          Returns:
              list: A list of dictionaries where each dictionary contains details of a VPN
              such as name, location, next charge date, public IP, status, uptime, CPU usage,
              and drive usage.
          """
        local_vpn_list = list()
        headers = {
            "accept": "application/json",
            "X-Authorization": self.auth(user_id=user_id),
            "Accept-Language": "ru",
        }
        request_list_vpn = self._send_request(endpoint="vpn/list", headers=headers)
        for vpn in request_list_vpn:
            time = datetime.utcfromtimestamp(vpn["plan"]["next_charge"]).strftime("%Y|%m|%d %H:%M:%S")
            vpn_info = {
                "id": vpn["id"],
                "name": vpn["name"],
                "location": vpn["location"]["name"],
                "next_charge": time,
                "ip": vpn["network"]["public_ip"],
                "status": vpn["status"]["name"],
                "uptime": vpn["status"]["message"],
                "cpu": vpn["status"]["cpu"]["value"],
                "drive": vpn["status"]["drive"]["value"]
            }
            local_vpn_list.append(vpn_info)
        return local_vpn_list
