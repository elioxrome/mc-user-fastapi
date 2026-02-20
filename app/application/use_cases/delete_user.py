from app.application.exceptions import UserNotFoundError
from app.application.ports.user_repository import UserRepository


class DeleteUserUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, user_id: str) -> None:
        if not self.user_repository.exists(user_id):
            raise UserNotFoundError(f"Usuario '{user_id}' no encontrado")

        self.user_repository.delete(user_id)
