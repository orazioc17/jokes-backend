from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import db_jokes
from .schemas import JokeDisplay, JokeCreation

router = APIRouter(
    prefix='/jokes',
    tags=['Jokes']
)


@router.get('', response_model=List[JokeDisplay])
def get_all_jokes(db: Session = Depends(get_db)):
    return db_jokes.get_all_jokes(db)


@router.post('', response_model=JokeDisplay)
def publish_joke(request: JokeCreation, db: Session = Depends(get_db)):
    return db_jokes.publish_joke(db, request)
