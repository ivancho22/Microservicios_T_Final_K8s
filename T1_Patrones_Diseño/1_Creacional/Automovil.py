class Automovil:
    def __init__(self):
        self.tipo_motor = None
        self.color = None
        self.llantas = None
        self.sonido = None
        self.interiores = None
        self.techo_solar = False
        self.gps = False

    def __str__(self):
        return (
            f"Automóvil:\n"
            f" Motor: {self.tipo_motor}\n"
            f" Color: {self.color}\n"
            f" Llantas: {self.llantas}\n"
            f" Sonido: {self.sonido}\n"
            f" Interiores: {self.interiores}\n"
            f" Techo solar: {'Sí' if self.techo_solar else 'No'}\n"
            f" GPS: {'Sí' if self.gps else 'No'}"
        )