#Notif. Type 2
from Notification import Notification

class AlertNotification(Notification):
    def send(self, message: str):
        self.platform.display(f"Alert: {message}")