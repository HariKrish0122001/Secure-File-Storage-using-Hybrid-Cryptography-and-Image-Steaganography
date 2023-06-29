import threading
from typing import Any


class ZCThreadUtil:
    def __init__(self) -> None:
        self.current_thread = threading.current_thread()

    def get_value(self, key: str):
        try:
            return getattr(self.current_thread, key)
        except AttributeError:
            return None

    def put_value(self, key: str, val: Any):
        setattr(self.current_thread, key, val)
