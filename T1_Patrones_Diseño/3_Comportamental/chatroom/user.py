from chatroom.interfaces import IChatRoom, BaseUser


class User(BaseUser):
    def __init__(self, name: str):
        self.name = name

    def send_message(self, message: str, chat_room: IChatRoom):
        if self not in chat_room.get_users():
            print(f"{self.name} does not belong to the room {chat_room.get_name()}")
            return

        print(
            f"{self.name} sends the message to the room {chat_room.get_name()}: {message}"
        )
        chat_room.send_message(message, self)

    def receive_message(self, message: str, sender: "User", chat_room_name: str):
        print(
            f"{self.name} receives the message from {sender.name} in the room {chat_room_name}: {message}"
        )

    def get_name(self):
        return self.name
