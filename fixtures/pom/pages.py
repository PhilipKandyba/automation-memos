import pytest

from core.web.entities.browser_page import BrowserPage
from pom.pages.login_page import AuthPage
from pom.pages.main_page import MainPage


@pytest.fixture()
def auth_page() -> AuthPage | BrowserPage:
    return AuthPage()


@pytest.fixture()
def main_page() -> MainPage:
    return MainPage()
