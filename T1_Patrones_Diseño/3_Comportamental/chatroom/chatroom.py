from chatroom.interfaces import IChatRoom, BaseUser


class ConcreteChatRoom(IChatRoom):
    """Concrete Mediator.

    Centralizes the communication between members (Users).
    """

    def __init__(self, name: str):
        self.name = name
        self._members: list[BaseUser] = []

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

    def send_message(self, message: str, sender: BaseUser):
        """Send a message to all users in the chat room except the sender."""
        for user in self._members:
            if user != sender:
                user.receive_message(message, sender, self.name)


class GeneralChatRoom(IChatRoom):
    """Represents a general group chat room."""

    def __init__(self, name: str):
        self.name = name
        self._members: list[BaseUser] = []

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

    def send_message(self, message: str, sender: BaseUser):
        """Send a message to all users in the chat room except the sender."""
        for user in self._members:
            if user != sender:
                user.receive_message(message, sender, self.name)


class PrivateChatRoom(IChatRoom):
    """Represents a private chat room between two users."""

    def __init__(self, name: str):
        self.name = name
        self._members: list[BaseUser] = []

    def get_name(self):
        """Get the name of the chat room."""
        return self.name

    def add_user(self, user):
        """Add a user to the chat room."""
        if user not in self._members and len(self._members) < 2:
            # Ensure only two users can be added to a private chat room
            return self._members.append(user)
        else:
            raise Exception("Private chat rooms can only have two members.")

    def remove_user(self, user):
        """Remove a user from the chat room."""
        if user in self._members:
            return self._members.remove(user)

    def get_users(self):
        """Get the list of users in the chat room."""
        return self._members

    def send_message(self, message: str, sender: BaseUser):
        """Send a message to all users in the chat room except the sender."""
        for user in self._members:
            if user != sender:
                user.receive_message(message, sender, self.name)
