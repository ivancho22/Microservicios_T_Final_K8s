from chatroom.chatroom import GeneralChatRoom, PrivateChatRoom
from chatroom.user import User

if __name__ == "__main__":
    # Crear instancias de salas de chat
    sala_general = GeneralChatRoom("General")
    sala_privada = PrivateChatRoom("Privada")

    # Crear instancias de usuarios
    juan = User("Juan")
    maria = User("María")
    ana = User("Ana")
    pedro = User("Pedro")

    # Agregar usuarios a las salas de chat
    sala_general.add_user(juan)
    sala_general.add_user(maria)
    sala_general.add_user(ana)

    sala_privada.add_user(juan)
    sala_privada.add_user(pedro)

    # Enviar mensajes entre los usuarios
    juan.send_message("Hola a todos en la sala general!", sala_general)
    maria.send_message("Hola, Juan! Bienvenidas a la sala general", sala_general)
    ana.send_message("Hola a todos!", sala_general)

    juan.send_message("¡Hola! Desde la sala privada", sala_privada)
    pedro.send_message("¡Hola Juan! En la sala privada", sala_privada)
