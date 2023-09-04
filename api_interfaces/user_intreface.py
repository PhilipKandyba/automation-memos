from functools import cached_property

from api_interfaces.auth_intreface import auth_interface
from config import Config
from core.api.interface import ApiInterface


class UserInterface(ApiInterface):
    def __init__(self, slug_prefix: str, username: str, password: str) -> None:
        self.slug_prefix = slug_prefix
        self.username = username
        self.password = password
        super().__init__(
            Config.BASE_URL + self.slug_prefix, cookies=self.access_cookies
        )

    @cached_property
    def user_token(self) -> str:
        return auth_interface.signin(
            username=self.username, password=self.password
        ).cookies[Config.access_cookie_name]

    @property
    def access_cookies(self) -> dict:
        return {Config.access_cookie_name: self.user_token}
