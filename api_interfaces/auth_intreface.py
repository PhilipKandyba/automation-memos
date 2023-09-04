from config import Config
from requests import Response
from core.api.interface import ApiInterface


class AuthInterface(ApiInterface):
    def __init__(self) -> None:
        self.slug_prefix = "/api/v1/auth"
        super().__init__(Config.BASE_URL)

    def signup(self, username: str, password: str, **kwargs) -> Response:
        data = {"username": username, "password": password}
        return self.post(slug=f"{self.slug_prefix}/signup", json=data, **kwargs)

    def signin(self, username: str, password: str, **kwargs) -> Response:
        data = {"username": username, "password": password}
        return self.post(slug=f"{self.slug_prefix}/signin", json=data, **kwargs)


auth_interface = AuthInterface()
