import pytest

from config import Config
from core import faker, teardown_queue
from entities.user import Admin, User
from pom.pages.main_page import MainPage


@pytest.fixture()
def admin() -> Admin:
    return Admin()


@pytest.fixture()
def user() -> User:
    admin = Admin()
    new_user = admin.create_user(
        username=faker.name(), password=faker.password()
    )
    teardown_queue.add(admin.delete_user, new_user.username)
    return new_user


@pytest.fixture()
def logged_user(user: User) -> User:
    main_page = MainPage()
    main_page.page.open().set_cookies(Config.access_cookie_name, user.login())
    return user
