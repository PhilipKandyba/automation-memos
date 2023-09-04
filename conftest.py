import allure
import pytest
from core.web.driver import driver
from api_interfaces.settings_inteface import SettingsInterface

pytest_plugins = [
    "fixtures.pom.pages",
    "fixtures.pom.elements",
    "fixtures.user",
    "core.driver_handler",
    "core.teardown_handler",
]


def pytest_sessionstart() -> None:
    SettingsInterface().allow_signup()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        if rep.failed:
            try:
                current_driver = driver["driver"]
                allure.attach(
                    current_driver.get_screenshot_as_png(),
                    name=item.name,
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception as e:
                print("Fail to take screen-shot: {}".format(e))
