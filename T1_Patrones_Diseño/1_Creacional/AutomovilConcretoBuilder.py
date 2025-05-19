from AutomovilBuilder import AutomovilBuilder
from Automovil import Automovil


class AutomovilConcretoBuilder(AutomovilBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._automovil = Automovil()

    def set_motor(self, tipo):
        self._automovil.tipo_motor = tipo
        return self

    def set_color(self, color):
        self._automovil.color = color
        return self

    def set_llantas(self, llantas):
        self._automovil.llantas = llantas
        return self

    def set_sonido(self, sonido):
        self._automovil.sonido = sonido
        return self

    def set_interiores(self, interiores):
        self._automovil.interiores = interiores
        return self

    def set_techo_solar(self, tiene):
        self._automovil.techo_solar = tiene
        return self

    def set_gps(self, tiene):
        self._automovil.gps = tiene
        return self

    def build(self):
        auto = self._automovil
        self.reset()  # opcional: reiniciar para el próximo auto
        return auto