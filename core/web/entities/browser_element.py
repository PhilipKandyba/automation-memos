import allure

from core.loggers.core_logger import core_log_decorator
from core.web.entities.wait import Wait
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from core import core_logger


class Locator:
    def __init__(self, by: str, selector: str) -> None:
        self._by = by
        self._selector = selector

    @property
    def by(self) -> str:
        return self._by

    @property
    def selector(self) -> str:
        return self._selector

    @property
    def locator(self) -> tuple:
        return self._by, self._selector

    def extend(self, selector: str, separator: str = " ") -> "Locator":
        return Locator(self._by, f"{self._selector}{separator}{selector}")


class BrowserElement:
    def __init__(self, driver: WebDriver, locator: tuple) -> None:
        self.locator = locator
        self.driver = driver
        self._wait = Wait(self.driver)

    def __repr__(self):
        return f"{self.locator}"

    @property
    def _element(self) -> WebElement:
        self._wait.for_visibility(self.locator)
        return self.driver.find_element(*self.locator)

    @core_log_decorator
    @allure.step("Wait for element invisibility {0}")
    def wait_for_visibility(self) -> WebElement:
        return self._wait.for_visibility(self._wait)

    @core_log_decorator
    @allure.step("Wait for element visibility {0}")
    def wait_for_invisibility(self) -> WebElement:
        return self._wait.for_visibility(self._wait)

    @core_log_decorator
    @allure.step("Element click {0}")
    def click(self) -> None:
        self._element.click()

    @core_log_decorator
    @allure.step("Element fill {0}, value: {text}")
    def fill(self, text: str) -> None:
        self._element.clear()
        self._element.send_keys(text)

    @core_log_decorator
    @allure.step("Is element present {0}")
    def is_present(self) -> bool:
        try:
            return self._wait.for_visibility(self.locator)
        except TimeoutException:
            return False

    @core_log_decorator
    @allure.step("Is not element present {0}")
    def is_not_present(self) -> bool:
        try:
            return self._wait.for_invisibility(self.locator)
        except TimeoutException:
            return False

    @core_log_decorator
    @allure.step("Getting test from element {0}")
    def get_text(self) -> str:
        return self._element.text

    @core_log_decorator
    @allure.step("Is element has text {0}, expected: {expected_text}")
    def has_text(self, expected_text: str) -> bool:
        return self.get_text() == expected_text
