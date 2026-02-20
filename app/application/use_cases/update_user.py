from app.application.exceptions import UserEmailAlreadyExistsError, UserNotFoundError
from app.application.ports.user_repository import UserRepository
from app.domain.user import User


class UpdateUserUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, user_id: str, name: str, email: str) -> User:
        if not self.user_repository.exists(user_id):
            raise UserNotFoundError(f"Usuario '{user_id}' no encontrado")

        if self.user_repository.exists_by_email(email):
            current_user = self.user_repository.get_by_id(user_id)
            if current_user and current_user.email != email:
                raise UserEmailAlreadyExistsError(f"Email '{email}' ya existe")

        user = User(id=user_id, name=name, email=email)
        return self.user_repository.update(user)
