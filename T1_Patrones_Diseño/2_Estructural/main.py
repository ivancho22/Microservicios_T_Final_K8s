from WebPlatform import WebPlatform
from MobilePlatform import MobilePlatform
from DesktopPlatform import DesktopPlatform
from ConfirmationNotification import ConfirmationNotification
from AlertNotification import AlertNotification
from WarningNotification import WarningNotification

# Client Code Example
if __name__ == "__main__":
    # Creating platforms / implementors
    web = WebPlatform()
    mobile = MobilePlatform()
    desktop = DesktopPlatform()
 
    # Creating notifications
    confirmation = ConfirmationNotification(web)
    alert = AlertNotification(mobile)
    warning = WarningNotification(desktop)
 
    # Sending notifications
    confirmation.send("Your order has been confirmed.")
    alert.send("Your order has been shipped.")
    warning.send("Your order is delayed.")