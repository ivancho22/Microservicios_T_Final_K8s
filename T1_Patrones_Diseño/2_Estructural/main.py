# Types of Platforms (3 so far, according to the scenario 2)
from WebPlatform import WebPlatform
from MobilePlatform import MobilePlatform
from DesktopPlatform import DesktopPlatform

# Types of Notifications (4 so far, according to the scenario 2)
from MessageNotification import MessageNotification
from ConfirmationNotification import ConfirmationNotification
from AlertNotification import AlertNotification
from WarningNotification import WarningNotification

# Example, Main

if __name__ == "__main__":
    # Create/implemetors
    web = WebPlatform()
    mobile = MobilePlatform()
    desktop = DesktopPlatform()
 
    # Create notific.
    message = MessageNotification(mobile)
    confirmation = ConfirmationNotification(web)
    alert = AlertNotification(mobile)
    warning = WarningNotification(desktop)

 
    # Test to send notific.
    message.send("Hola! Tenemos descuentos en laptops solo por hoy.")
    confirmation.send("Tu pedido ha sido enviado exitosamente.")
    alert.send("Tu pedido está en camino.")
    warning.send("Tu pedido está retrasado!")