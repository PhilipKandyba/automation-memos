from api_interfaces.auth_intreface import auth_interface
from config import Config
from requests import Response
from core.api.interface import ApiInterface, ApiCallException


class AdminInterface(ApiInterface):
    def __init__(self: "AdminInterface") -> None:
        self.admin_token = self.get_admin_token()
        super().__init__(
            Config.BASE_URL,
            cookies={Config.access_cookie_name: self.admin_token},
        )

    @staticmethod
    def get_admin_token() -> str:
        try:
            token_request = auth_interface.signin(
                Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD
            )
        except ApiCallException:
            token_request = auth_interface.signup(
                Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD
            )
        return token_request.cookies[Config.access_cookie_name]

    def get_users(self, **kwargs) -> Response:
        return self.get(slug="/api/v1/user", **kwargs)

    def delete_user(self, user_id: int, **kwargs) -> Response:
        return self.delete(
            slug=f"/api/v1/user/{user_id}",
            **kwargs,
        )


admin_interface = AdminInterface()
