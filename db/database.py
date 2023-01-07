from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./jokes.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Anytime we perform any operation on the database, we're going to get the session, we're going to use it,
    and then we close it, so we don't have to worry about that any longer
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()