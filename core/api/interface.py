from typing import Literal

import requests
from requests import Response

from core.loggers.core_logger import core_log_decorator

METHODS = Literal["get", "post", "put", "delete"]


class ApiCallException(Exception):
    pass


class ApiInterface:
    def __init__(self, base_url: str, **kwargs) -> None:
        self.base_url = base_url
        self.kwargs = kwargs

    @core_log_decorator
    def make_request(
        self, method: METHODS, url: str, **kwargs: dict
    ) -> Response:
        response = requests.request(method, url, **kwargs, **self.kwargs)
        if not response.ok:
            raise ApiCallException(
                response.status_code, response.text, response.cookies.get_dict()
            )
        return response

    def get(self, slug: str, **kwargs) -> Response:
        return self.make_request(
            method="get", url=f"{self.base_url}{slug}", **kwargs
        )

    def post(self, slug: str, **kwargs) -> Response:
        return self.make_request(
            method="post", url=f"{self.base_url}{slug}", **kwargs
        )

    def delete(self, slug: str, **kwargs) -> Response:
        return self.make_request(
            method="delete", url=f"{self.base_url}{slug}", **kwargs
        )
