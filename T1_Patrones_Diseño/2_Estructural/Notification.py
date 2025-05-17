from abc import ABC, abstractmethod
from platform_ import Platform
# Abstraction - Notification
class Notification(ABC):
    def __init__(self, platform: Platform):
        self.platform = platform
 
    @abstractmethod
    def send(self, message: str):
        pass