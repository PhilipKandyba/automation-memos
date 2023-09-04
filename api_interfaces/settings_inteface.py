from api_interfaces.admin_intreface import AdminInterface
from requests import Response


class SettingsInterface(AdminInterface):
    def __init__(self: "SettingsInterface") -> None:
        self.slug_prefix = "/api/v1/system/setting"
        super().__init__()

    def allow_signup(self, **kwargs) -> Response:
        return self.post(
            slug=self.slug_prefix,
            json={"name": "allow-signup", "value": "true"},
            **kwargs
        )


settings_interface = SettingsInterface()
