#Platform Type 1
from Platform_ import Platform

class WebPlatform(Platform):
    def display(self, message: str):
        print(f"[WEB] {message}")