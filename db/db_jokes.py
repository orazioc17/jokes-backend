from datetime import datetime

from sqlalchemy.orm.session import Session

from .models import DbJoke
from routers.schemas import JokeCreation


def get_all_jokes(db: Session):
    return db.query(DbJoke).all()


def publish_joke(db: Session, request: JokeCreation):
    new_joke = DbJoke(
        title=request.title,
        text=request.text,
        up_votes=0,
        down_votes=0,
        created_at=datetime.now(),
        user_id=request.user_id
    )

    db.add(new_joke)
    db.commit()
    db.refresh(new_joke)

    return new_joke
