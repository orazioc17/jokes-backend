from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from .models import DbUser
from routers.schemas import UserCreation
from .hashing import Hash


def create_user(db: Session, request: UserCreation):

    if db.query(DbUser).filter(DbUser.username == request.username).first():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"The username {request.username} is already in use"
        )

    if db.query(DbUser).filter(DbUser.email == request.email).first():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"The email {request.email} is already in use"
        )

    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_all_users(db: Session):
    return db.query(DbUser).all()
