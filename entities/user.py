from api_interfaces.admin_intreface import admin_interface
from api_interfaces.auth_intreface import auth_interface
from config import Config
from entities.memo import Memos
from enums import UserRoles


class Admin:
    @staticmethod
    def create_user(username: str, password: str) -> "User":
        return User(
            password=password,
            **auth_interface.signup(username, password).json()
        )

    @staticmethod
    def get_users() -> list["User"]:
        return [User(**user) for user in admin_interface.get_users().json()]

    def get_user(self, username: str) -> "User":
        for user in self.get_users():
            if user.username == username:
                return user

    def delete_user(self, username: str) -> None:
        user = self.get_user(username)
        admin_interface.delete_user(user.user_id)

    def delete_all_users(self) -> None:
        for user in self.get_users():
            if not user.is_host:
                self.delete_user(user.username)


class User:
    def __init__(self, **kwargs) -> None:
        self.user_id = kwargs.get("id")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.is_host = kwargs.get("role") == UserRoles.HOST

    @property
    def memos(self) -> "Memos":
        return Memos(self)

    def login(self) -> str:
        return auth_interface.signin(self.username, self.password).cookies[
            Config.access_cookie_name
        ]
