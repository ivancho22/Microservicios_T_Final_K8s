from AutomovilBuilder import AutomovilBuilder

class Director:
    def __init__(self, builder: AutomovilBuilder):
        self._builder = builder

    def construir_auto_de_lujo(self):
        return (
            self._builder
            .set_motor("V8")
            .set_color("Negro")
            .set_llantas("Aleación 20''")
            .set_sonido("Bose Premium")
            .set_interiores("Cuero")
            .set_techo_solar(True)
            .set_gps(True)
            .build()
        )

    def construir_auto_basico(self):
        return (
            self._builder
            .set_motor("4 cilindros")
            .set_color("Blanco")
            .set_llantas("Acero 16''")
            .set_sonido("Estándar")
            .set_interiores("Tela")
            .set_techo_solar(False)
            .set_gps(False)
            .build()
        )