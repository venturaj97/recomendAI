# app/schemas.py
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    description: str
    release_date: datetime

class MovieCreate(MovieBase):
    pass

class MovieRead(MovieBase):
    id: int

    class Config:
        orm_mode = True

class RatingBase(BaseModel):
    rating: int
    user_id: int
    movie_id: int

class RatingCreate(RatingBase):
    pass

class RatingRead(RatingBase):
    id: int

    class Config:
        orm_mode = True
