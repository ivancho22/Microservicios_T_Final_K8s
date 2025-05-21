#Platform Type 2
from Platform_ import Platform

class MobilePlatform(Platform):
    def display(self, message: str):
        print(f"[MOBILE] {message}")