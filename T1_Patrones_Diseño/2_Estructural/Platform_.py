# Platform I
from abc import ABC, abstractmethod

# Implementor - Platform
class Platform(ABC):
    @abstractmethod
    def display(self, message: str):
        pass
