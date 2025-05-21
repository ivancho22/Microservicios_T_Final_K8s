#Notif. Type 4
from Notification import Notification

class ConfirmationNotification(Notification):
    def send(self, message: str):
        self.platform.display(f"Confirmation: {message}")
 