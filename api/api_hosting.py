from api.client import ClientHttp
from utils.config import cache
from utils.logger import logger


class APIHosting(ClientHttp):
    def auth(self, email: str, password: str, user_id: str) -> str:
        """
        Authenticate the user and retrieve a token.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.
            user_id (str): The user ID.

        Returns:
            str: The authentication token.
        """
        token_user = cache.get(user_id)
        if token_user is None:
            try:
                auth_data = {
                    "type": "password",
                    "email": email,
                    "password": password,
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
