from typing import Dict, Optional

from app.application.ports.user_repository import UserRepository
from app.domain.user import User


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self._users: Dict[str, User] = {}

    def create(self, user: User) -> User:
        self._users[user.id] = user
        return user

    def update(self, user: User) -> User:
        self._users[user.id] = user
        return user

    def delete(self, user_id: str) -> None:
        del self._users[user_id]

    def exists_by_email(self, email: str) -> bool:
        return any(user.email == email for user in self._users.values())

    def exists(self, user_id: str) -> bool:
        return user_id in self._users

    def get_by_id(self, user_id: str) -> Optional[User]:
        return self._users.get(user_id)
