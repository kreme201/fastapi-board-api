from fastapi import APIRouter, HTTPException
from starlette import status

from app.models import User
from app.services import password
from app.web.user.dtos import UserResponse, UserCreateDto, UserUpdateDto
from database import transactional

router = APIRouter()


@router.get("/", response_model=list[UserResponse])
@transactional
def get_all_users():
    return User.query.all()


@router.post("/", response_model=UserResponse)
@transactional
def create_user(dto: UserCreateDto):
    if User.query.filter(User.email == dto.email).first() is not None:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="User Already Exists.")

    return User(
        name=dto.name,
        email=dto.email,
        password=password.hash(dto.password),
    ).save()


@router.get("/{user_id}", response_model=UserResponse)
@transactional
def get_user(user_id: int):
    user = User.query.filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User Not Found")

    return user


@router.put("/{user_id}", response_model=UserResponse)
@transactional
def update_user(user_id: int, dto: UserUpdateDto):
    user = User.query.filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User Not Found")

    if dto.name is not None:
        user.name = dto.name

    if dto.password is not None:
        user.password = password.hash(dto.password)

    return user.save()


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@transactional
def delete_user(user_id: int):
    user = User.query.filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User Not Found.")

    user.delete()
