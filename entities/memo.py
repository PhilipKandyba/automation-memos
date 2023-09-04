from api_interfaces.memo_intreface import MemoInterface


class Memos:
    def __init__(self, user: "User") -> None:
        self.memo_interface = MemoInterface(user.username, user.password)

    def get_memos(self) -> list["Memo"]:
        return [
            Memo(self.memo_interface, **memo_data)
            for memo_data in self.memo_interface.get_memos().json()
        ]

    def delete_all(self) -> None:
        for memo in self.get_memos():
            memo.delete()

    def create_memo(self, content: str) -> "Memo":
        return Memo(
            self.memo_interface,
            **self.memo_interface.create_memo(content=content).json()
        )


class Memo:
    def __init__(self, memo_interface: MemoInterface, **kwargs) -> None:
        self.memo_id = kwargs.get("id")
        self.memo_interface = memo_interface

    def delete(self) -> None:
        self.memo_interface.delete_memo(memo_id=self.memo_id)
