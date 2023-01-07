from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from .schemas import UserCreation, UserDisplay
from db.database import get_db
from db import db_user


router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.post('', response_model=UserDisplay)
def create_user(request: UserCreation, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


@router.get('', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)
