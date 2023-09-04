from requests import Response
from enums import MemosVisibility
from api_interfaces.user_intreface import UserInterface


class MemoInterface(UserInterface):
    def __init__(self, username: str, password: str) -> None:
        self.slug_prefix = "/api/v1/memo"
        self.username = username
        self.password = password
        super().__init__(self.slug_prefix, username, password)

    def get_memos(self, **kwargs) -> Response:
        return self.get("", **kwargs)

    def delete_memo(self, memo_id: int, **kwargs) -> Response:
        return self.delete(slug=f"/{memo_id}", **kwargs)

    def create_memo(
        self,
        content: str,
        visibility: str = MemosVisibility.PRIVATE,
        **kwargs: dict,
    ) -> Response:
        payload = {
            "content": content,
            "visibility": visibility,
            "relationList": [],
            "resourceIdList": [],
        }
        return self.post(slug="", json=payload, **kwargs)
