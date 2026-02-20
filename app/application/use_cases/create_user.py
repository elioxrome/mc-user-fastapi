from uuid import uuid4

from app.application.exceptions import UserEmailAlreadyExistsError
from app.application.ports.user_repository import UserRepository
from app.domain.user import User


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, name: str, email: str) -> User:
        if self.user_repository.exists_by_email(email):
            raise UserEmailAlreadyExistsError(f"Email '{email}' ya existe")

        user = User(id=str(uuid4()), name=name, email=email)
        return self.user_repository.create(user)
