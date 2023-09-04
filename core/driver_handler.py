import pytest
from core.web.driver import driver


def pytest_configure(config) -> None:
    config.pluginmanager.register(DriverHandler())


class DriverHandler:
    @pytest.hookimpl(tryfirst=True)
    def pytest_sessionfinish(self) -> None:
        driver["driver"].quit()
