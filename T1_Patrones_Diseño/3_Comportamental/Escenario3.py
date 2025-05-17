from abc import ABC, abstractmethod


class ChatRoom(ABC):
    """Interface Mediador.

    Define the send_message method to communicate with chat members.
    """

    @abstractmethod
    def get_name(self) -> str: ...

    @abstractmethod
    def add_user(self, user: "User") -> None: ...

    @abstractmethod
    def remove_user(self, user: "User") -> None: ...

    @abstractmethod
    def get_users(self) -> list["User"]: ...

    @abstractmethod
    def send_message(self, message: str, sender: "User") -> None: ...


class ConcreteChatRoom(ChatRoom):
    """Concrete Mediator.

    Centralizes the communication between members (Users).
    """

    def __init__(self, name: str):
        self.name = name
        self._members: list["User"] = []

    def get_name(self):
        """Get the name of the chat room."""
        return self.name

    def add_user(self, user):
        """Add a user to the chat room."""
        if user not in self._members:
            return self._members.append(user)

    def remove_user(self, user):
        """Remove a user from the chat room."""
        if user in self._members:
            return self._members.remove(user)

    def get_users(self):
        """Get the list of users in the chat room."""
        return self._members

    def send_message(self, message: str, sender: "User"):
        """Send a message to all users in the chat room except the sender."""
        for user in self._members:
            if user != sender:
                user.receive_message(message, sender, self.name)


class User:
    """Chat member.

    Uses mediator to send messages.
    """

    def __init__(self, name: str):
        self.name = name

    def send_message(self, message: str, chat_room: ChatRoom):
        """Send a message to a specific chat room."""
        if self not in chat_room.get_users():
            print(f"{self.name} does not belong to the room {chat_room.get_name()}")
            return

        print(
            f"{self.name} sends the message to the room {chat_room.get_name()}: {message}"
        )
        chat_room.send_message(message, self)

    def receive_message(self, message: str, sender: "User", chat_room_name: str):
        """Receive a message from another user."""
        print(
            f"{self.name} receives the message from {sender.name} in the room {chat_room_name}: {message}"
        )

    def get_name(self):
        """Get the name of the user."""
        return self.name


if __name__ == "__main__":
    # Crear las salas de chat (mediadores)
    sala_general = ConcreteChatRoom("General")
    sala_privada = ConcreteChatRoom("Privada")

    # Crear los usuarios
    juan = User("Juan")
    maria = User("María")
    ana = User("Ana")
    pedro = User("Pedro")

    # Los usuarios se unen a las salas de chat
    sala_general.add_user(juan)
    sala_general.add_user(maria)
    sala_general.add_user(ana)

    sala_privada.add_user(juan)
    sala_privada.add_user(pedro)

    # Los usuarios envían mensajes a las salas de chat
    juan.send_message("Hola a todos en la sala general!", sala_general)
    maria.send_message("Hola, Juan! Bienvenidas a la sala general", sala_general)
    ana.send_message("Hola a todos!", sala_general)

    juan.send_message("¡Hola! Desde la sala privada", sala_privada)
    pedro.send_message("¡Hola Juan! En la sala privada", sala_privada)
