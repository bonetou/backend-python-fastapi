from sqlalchemy.orm import Session
from .dtos import CreateUserDto
from .models import User


def create_user_service(create_user_dto: CreateUserDto, session: Session):
    user_already_exists = (
        session.query(User)
        .filter_by(username=create_user_dto.username)
        .first()
    )
    if user_already_exists:
        raise Exception("Username already exists")

    user = User(username=create_user_dto.username,
                password=create_user_dto.password)
    session.add(user)
    session.commit()
