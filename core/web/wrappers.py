from typing import Callable

from core.web.driver import get_driver
from core.web.entities.browser_page import BrowserPage
from core.web.entities.browser_element import BrowserElement, Locator


def page(**kwargs) -> Callable:
    def _wrapper(original_class: object) -> object:
        driver = get_driver()
        for attribute, value in original_class.__dict__.items():
            if isinstance(value, tuple):
                setattr(
                    original_class, attribute, BrowserElement(driver, value)
                )
            elif isinstance(value, Locator):
                setattr(
                    original_class,
                    attribute,
                    BrowserElement(driver, value.locator),
                )
        if kwargs.get("url"):
            original_class.page = BrowserPage(driver, **kwargs)
        return original_class

    return _wrapper
