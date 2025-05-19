from AutomovilConcretoBuilder import AutomovilConcretoBuilder
from Director import Director



if __name__ == "__main__":
    builder = AutomovilConcretoBuilder()
    director = Director(builder)

    print("=== Auto de Lujo ===")
    auto_lujo = director.construir_auto_de_lujo()
    print(auto_lujo)

    print("\n=== Auto Básico ===")
    auto_basico = director.construir_auto_basico()
    print(auto_basico)

    print("\n=== Auto Personalizado ===")
    auto_custom = (
        builder
        .set_motor("Híbrido")
        .set_color("Rojo")
        .set_llantas("Deportivas 18''")
        .set_sonido("JBL")
        .set_interiores("Mixto cuero-tela")
        .set_techo_solar(True)
        .set_gps(False)
        .build()
    )
    print(auto_custom)