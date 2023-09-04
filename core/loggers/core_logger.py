import logging
import re
import sys
from logging import FileHandler, StreamHandler, Formatter

from core.enums import Regexps


class SensitiveFormatter(logging.Formatter):
    @staticmethod
    def _filter(s):
        return re.sub(
            Regexps.JWT_PATTERN,
            "*****",
            s,
        )

    def format(self, record):
        original = logging.Formatter.format(self, record)
        return self._filter(original)


log_format = Formatter(fmt="[%(asctime)s: %(levelname)s] %(message)s")

core_logger = logging.getLogger("core_logger")
core_logger.setLevel(logging.DEBUG)

file_handler = FileHandler(filename=f"core_logger.log")
file_handler.setFormatter(
    SensitiveFormatter("[%(asctime)s: %(levelname)s] %(message)s")
)
core_logger.addHandler(file_handler)

stream_handler = StreamHandler(stream=sys.stdout)
stream_handler.setFormatter(
    SensitiveFormatter("[%(asctime)s: %(levelname)s] %(message)s")
)
core_logger.addHandler(stream_handler)


def core_log_decorator(func):
    def _wrapper(*args, **kwargs):
        msg = ""
        if args:
            if hasattr(args[0], "__dict__"):
                msg = f"Calling {args[0].__class__.__name__}.{func.__name__}: "
        else:
            msg = f"Calling function {func.__name__} (args): "

        for arg in args:
            if hasattr(arg, "__dict__"):
                for name, value in arg.__dict__.items():
                    if not hasattr(value, "__dict__"):
                        msg += f"{name}: {value}, "
            else:
                msg += f" {arg},"

        if kwargs:
            msg += f" (kwargs): {kwargs}"

        result = func(*args, **kwargs)
        if result:
            msg += f" | result: {result}"
        core_logger.info(msg)

        return result

    return _wrapper
