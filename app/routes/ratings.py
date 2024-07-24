# app/routes/ratings.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from app.models import Rating
from app.schemas import RatingCreate, RatingRead
from app.database import get_session

router = APIRouter()

@router.post("/", response_model=RatingRead)
def create_rating(*, session: Session = Depends(get_session), rating: RatingCreate):
    db_rating = Rating.model_validate(rating)
    session.add(db_rating)
    session.commit()
    session.refresh(db_rating)
    return db_rating

@router.get("/", response_model=list[RatingRead])
def read_ratings(*, session: Session = Depends(get_session)):
    ratings = session.exec(select(Rating)).all()
    return ratings

@router.get("/{rating_id}", response_model=RatingRead)
def read_rating(*, session: Session = Depends(get_session), rating_id: int):
    rating = session.get(Rating, rating_id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    return rating

@router.put("/{rating_id}", response_model=RatingRead)
def update_rating(*, session: Session = Depends(get_session), rating_id: int, rating: RatingCreate):
    db_rating = session.get(Rating, rating_id)
    if not db_rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    db_rating.rating = rating.rating
    db_rating.user_id = rating.user_id
    db_rating.movie_id = rating.movie_id
    session.add(db_rating)
    session.commit()
    session.refresh(db_rating)
    return db_rating

@router.delete("/{rating_id}", response_model=RatingRead)
def delete_rating(*, session: Session = Depends(get_session), rating_id: int):
    db_rating = session.get(Rating, rating_id)
    if not db_rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    session.delete(db_rating)
    session.commit()
    return db_rating
