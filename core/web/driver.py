import os
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = {}


def get_driver() -> WebDriver:
    browser_constructor = {
        "chrome": lambda: webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        ),
        "remote": lambda: webdriver.Remote(
            command_executor=os.environ.get("SELENIUM_HUB_HOST"),
            options=webdriver.ChromeOptions(),
        ),
    }.get(os.environ["BROWSER"])
    if not driver.get("driver"):
        driver["driver"] = browser_constructor()
    return driver["driver"]
