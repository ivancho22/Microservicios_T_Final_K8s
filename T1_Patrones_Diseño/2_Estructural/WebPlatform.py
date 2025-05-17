from platform_ import Platform

class WebPlatform(Platform):
    def display(self, message: str):
        print(f"[WEB] {message}")