from pydantic import BaseModel, EmailStr


class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr


class UpdateUserRequest(BaseModel):
    name: str
    email: EmailStr


class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr


class HealthResponse(BaseModel):
    status: str
