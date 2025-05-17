from platform_ import Platform
class DesktopPlatform(Platform):
    def display(self, message: str):
        print(f"[DESKTOP] {message}")