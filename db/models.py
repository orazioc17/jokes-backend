from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class DbUser(Base):

    # To create a table, we have to provide it a name first
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)  # This id will be automatically created and increased
    username = Column(String)
    email = Column(String)
    password = Column(String)
    jokes = relationship("DbJoke", back_populates="user")  # This back populates with the field "user" from DbArticle


class DbJoke(Base):
    __tablename__ = "jokes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    up_votes = Column(Integer)
    down_votes = Column(Integer)
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("DbUser", back_populates="jokes")  # This back populates with the field "items" from DbUser
