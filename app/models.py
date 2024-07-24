# app/models.py
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    ratings: List["Rating"] = Relationship(back_populates="user")

class Movie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    release_date: datetime
    ratings: List["Rating"] = Relationship(back_populates="movie")

class Rating(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rating: int
    user_id: int = Field(foreign_key="user.id")
    movie_id: int = Field(foreign_key="movie.id")
    user: User = Relationship(back_populates="ratings")
    movie: Movie = Relationship(back_populates="ratings")
