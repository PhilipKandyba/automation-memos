import os
from selenium.webdriver.chrome.webdriver import WebDriver


class BrowserPage:
    def __init__(self, driver: WebDriver, **kwargs) -> None:
        self.driver = driver
        self.url = f'{os.getenv("BASE_URL")}{kwargs.get("url", "")}'

    def open(self) -> "BrowserPage":
        self.driver.get(self.url)
        return self

    def set_cookies(self, name: str, value: str) -> "BrowserPage":
        self.driver.add_cookie(cookie_dict={"name": name, "value": value})
        return self
