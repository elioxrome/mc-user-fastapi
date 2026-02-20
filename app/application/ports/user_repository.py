from abc import ABC, abstractmethod
from typing import Optional

from app.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, user_id: str) -> None:
        pass

    @abstractmethod
    def exists_by_email(self, email: str) -> bool:
        pass

    @abstractmethod
    def exists(self, user_id: str) -> bool:
        pass

    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[User]:
        pass
