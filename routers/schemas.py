from datetime import datetime
from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreation(UserBase):
    password: str


class JokeBase(BaseModel):
    title: str
    text: str


class UserInJoke(UserBase):
    id: int

    class Config:
        orm_mode = True


class JokeInUser(JokeBase):
    id: int
    up_votes: int
    down_votes: int
    created_at: datetime

    class Config:
        orm_mode = True


class JokeDisplay(JokeInUser):
    user: UserInJoke

    class Config:
        orm_mode = True


class UserDisplay(UserBase):
    id: int
    jokes: List[JokeInUser] = []

    class Config:
        orm_mode = True


class JokeCreation(JokeBase):
    user_id: int



