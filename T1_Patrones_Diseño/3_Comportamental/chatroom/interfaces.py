from abc import ABC, abstractmethod


class BaseUser(ABC):
    """Base for the user instances.

    Define the send_message and receive_message methods to communicate with the chat room.
    """

    @abstractmethod
    def send_message(self, message: str, chat_room: "IChatRoom") -> None: ...

    @abstractmethod
    def receive_message(
        self, message: str, sender: "BaseUser", chat_room_name: str
    ) -> None: ...

    @abstractmethod
    def get_name(self) -> str: ...


class IChatRoom(ABC):
    """Interface Mediador.

    Define the send_message method to communicate with chat members.
    """

    @abstractmethod
    def get_name(self) -> str: ...

    @abstractmethod
    def add_user(self, user: BaseUser) -> None: ...

    @abstractmethod
    def remove_user(self, user: BaseUser) -> None: ...

    @abstractmethod
    def get_users(self) -> list[BaseUser]: ...

    @abstractmethod
    def send_message(self, message: str, sender: BaseUser) -> None: ...
