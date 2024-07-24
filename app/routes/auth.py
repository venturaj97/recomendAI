# app/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session
from passlib.context import CryptContext

from app.models import User
from app.database import get_session

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

@router.post("/register")
def register(username: str, email: str, password: str, session: Session = Depends(get_session)):
    hashed_password = get_password_hash(password)
    user = User(username=username, email=email, password=hashed_password)
    try:
        session.add(user)
        session.commit()
        session.refresh(user)
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=400, detail="Username or email already registered")
    return user
