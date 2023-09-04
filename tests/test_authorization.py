from core import faker, teardown_queue
from entities.user import User, Admin
from pom.elements.navigation_element import NavigationElement
from pom.pages.login_page import AuthPage
from pom.pages.main_page import MainPage
import allure


def test_signin(
    user: User,
    auth_page: AuthPage,
    main_page: MainPage,
    nav_element: NavigationElement,
):
    """
    CaseId: 1
    """
    auth_page.page.open()
    auth_page.LOGIN_FIELD.fill(text=user.username)
    auth_page.PASSWORD_FIELD.fill(text=user.password)
    auth_page.SIGN_IN_BUTTON.click()

    assert main_page.EDITOR_CONTAINER.is_present()
    assert nav_element.USERNAME_LABEL.has_text(expected_text=user.username)


def test_signup(
    admin: Admin,
    auth_page: AuthPage,
    main_page: MainPage,
    nav_element: NavigationElement,
):
    """
    CaseId: 2
    """
    username, password = faker.name(), faker.password()

    auth_page.page.open()
    auth_page.LOGIN_FIELD.fill(text=username)
    auth_page.PASSWORD_FIELD.fill(text=password)
    auth_page.SIGN_UP_BUTTON.click()

    assert main_page.EDITOR_CONTAINER.is_present()
    assert nav_element.USERNAME_LABEL.has_text(expected_text=username)
    teardown_queue.add(admin.delete_user, username)
