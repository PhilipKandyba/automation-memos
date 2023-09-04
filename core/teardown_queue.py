from typing import Callable


class TeardownQueue:
    def __init__(self) -> None:
        self.teardown_queue_list = set()

    def add(self, func: Callable, *args, **kwargs) -> None:
        return self.teardown_queue_list.add(lambda: func(*args, **kwargs))

    def get_list(self) -> set:
        return self.teardown_queue_list
