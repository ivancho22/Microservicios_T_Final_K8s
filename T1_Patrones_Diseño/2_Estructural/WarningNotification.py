#Notif. Type 3
from Notification import Notification

class WarningNotification(Notification):
    def send(self, message: str):
        self.platform.display(f"Warning: {message}")
