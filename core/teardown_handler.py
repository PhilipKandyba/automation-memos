import pytest

from core import teardown_queue


def pytest_configure(config) -> None:
    config.pluginmanager.register(TeardownHandler())


class TeardownHandler:
    @pytest.hookimpl(trylast=True)
    def pytest_runtest_teardown(self) -> None:
        queue = teardown_queue.get_list()
        while queue:
            func = queue.pop()
            func()
