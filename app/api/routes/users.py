from fastapi import APIRouter, Depends, HTTPException, status

from app.api.schemas import CreateUserRequest, UpdateUserRequest, UserResponse
from app.application.exceptions import UserEmailAlreadyExistsError, UserNotFoundError
from app.application.use_cases.create_user import CreateUserUseCase
from app.application.use_cases.delete_user import DeleteUserUseCase
from app.application.use_cases.update_user import UpdateUserUseCase
from app.dependencies import (
    get_create_user_use_case,
    get_delete_user_use_case,
    get_update_user_use_case,
)

router = APIRouter(prefix="/api/v1/users", tags=["users"])


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    payload: CreateUserRequest,
    use_case: CreateUserUseCase = Depends(get_create_user_use_case),
) -> UserResponse:
    try:
        user = use_case.execute(name=payload.name, email=payload.email)
    except UserEmailAlreadyExistsError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc

    return UserResponse(id=user.id, name=user.name, email=user.email)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: str,
    payload: UpdateUserRequest,
    use_case: UpdateUserUseCase = Depends(get_update_user_use_case),
) -> UserResponse:
    try:
        user = use_case.execute(user_id=user_id, name=payload.name, email=payload.email)
    except UserNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except UserEmailAlreadyExistsError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc

    return UserResponse(id=user.id, name=user.name, email=user.email)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: str,
    use_case: DeleteUserUseCase = Depends(get_delete_user_use_case),
) -> None:
    try:
        use_case.execute(user_id=user_id)
    except UserNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
