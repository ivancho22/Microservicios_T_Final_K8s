#Notif. Type 1
from Notification import Notification

class MessageNotification(Notification):
    def send(self, message: str):
        self.platform.display(f"Message: {message}")
 