from abc import ABC, abstractmethod

class AutomovilBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_motor(self, tipo):
        pass

    @abstractmethod
    def set_color(self, color):
        pass

    @abstractmethod
    def set_llantas(self, llantas):
        pass

    @abstractmethod
    def set_sonido(self, sonido):
        pass

    @abstractmethod
    def set_interiores(self, interiores):
        pass

    @abstractmethod
    def set_techo_solar(self, tiene):
        pass

    @abstractmethod
    def set_gps(self, tiene):
        pass

    @abstractmethod
    def build(self):
        pass
