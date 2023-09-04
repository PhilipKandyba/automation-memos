from core.web.entities.browser_element import BrowserElement
from core.web.wrappers import page
from core import by


@page(url="/auth")
class AuthPage:
    LOGIN_FIELD: BrowserElement = (
        by.CSS_SELECTOR,
        'input[placeholder="Username"]',
    )
    PASSWORD_FIELD: BrowserElement = (
        by.CSS_SELECTOR,
        'input[placeholder="Password"]',
    )
    SIGN_UP_BUTTON: BrowserElement = (
        by.XPATH,
        '//button[contains(text(),"Sign up")]',
    )
    SIGN_IN_BUTTON: BrowserElement = (
        by.XPATH,
        '//button[contains(text(),"Sign in")]',
    )
