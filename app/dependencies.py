from app.application.use_cases.create_user import CreateUserUseCase
from app.application.use_cases.delete_user import DeleteUserUseCase
from app.application.use_cases.update_user import UpdateUserUseCase
from app.infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository

user_repository = InMemoryUserRepository()


def get_create_user_use_case() -> CreateUserUseCase:
    return CreateUserUseCase(user_repository)


def get_update_user_use_case() -> UpdateUserUseCase:
    return UpdateUserUseCase(user_repository)


def get_delete_user_use_case() -> DeleteUserUseCase:
    return DeleteUserUseCase(user_repository)
