# app/routes/movies.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.models import Movie
from app.schemas import MovieCreate, MovieRead
from app.database import get_session

router = APIRouter()

@router.post("/", response_model=MovieRead)
def create_movie(*, session: Session = Depends(get_session), movie: MovieCreate):
    db_movie = Movie.model_validate(movie)
    session.add(db_movie)
    session.commit()
    session.refresh(db_movie)
    return db_movie

@router.get("/", response_model=list[MovieRead])
def read_movies(*, session: Session = Depends(get_session)):
    movies = session.exec(select(Movie)).all()
    return movies

@router.get("/{movie_id}", response_model=MovieRead)
def read_movie(*, session: Session = Depends(get_session), movie_id: int):
    movie = session.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie
