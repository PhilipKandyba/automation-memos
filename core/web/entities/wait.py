from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class Wait:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def for_visibility(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator)
        )

    def for_invisibility(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located(locator)
        )
