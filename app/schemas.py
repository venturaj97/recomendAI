# app/schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True


class MovieBase(BaseModel):
    title: str
    description: Optional[str] = None
    release_date: Optional[str] = None

class MovieCreate(MovieBase):
    pass

class MovieRead(MovieBase):
    id: int

    class Config:
        from_attributes = True  # Atualizado para V2 do Pydantic


class RatingBase(BaseModel):
    title: str
    description: Optional[str] = None
    release_date: Optional[str] = None

class RatingCreate(RatingBase):
    pass

class RatingRead(RatingBase):
    id: int

    class Config:
        from_attributes = True  # Atualizado para V2 do Pydantic


