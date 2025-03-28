# app/routes/movies.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from app.models import Movie
from app.schemas import MovieCreate, MovieRead
from app.database import get_session
from app.tmdb_client import fetch_movie_details, search_movies

router = APIRouter()

@router.post("/", response_model=MovieRead)
def create_movie(*, session: Session = Depends(get_session), movie: MovieCreate):
    db_movie = Movie.model_validate(movie)
    session.add(db_movie)
    session.commit()
    session.refresh(db_movie)
    return db_movie

@router.put("/{movie_id}", response_model=MovieRead)
def update_movie(*, session: Session = Depends(get_session), movie_id: int, movie: MovieCreate):
    db_movie = session.get(Movie, movie_id)
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db_movie.title = movie.title
    db_movie.description = movie.description
    db_movie.release_date = movie.release_date
    session.add(db_movie)
    session.commit()
    session.refresh(db_movie)
    return db_movie

@router.delete("/{movie_id}", response_model=MovieRead)
def delete_movie(*, session: Session = Depends(get_session), movie_id: int):
    db_movie = session.get(Movie, movie_id)
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    session.delete(db_movie)
    session.commit()
    return db_movie

@router.get("/", response_model=List[MovieRead])
async def read_movies(*, session: Session = Depends(get_session)):
    movies = session.exec(select(Movie)).all()
    return movies

@router.get("/{movie_id}", response_model=MovieRead)
async def read_movie(*, session: Session = Depends(get_session), movie_id: int):
    movie = session.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.get("/search/{query}")
async def search_movies_endpoint(query: str):
    movies = await search_movies(query)
    return movies

@router.get("/details/{movie_id}")
async def get_movie_details(movie_id: int):
    movie_details = await fetch_movie_details(movie_id)
    return movie_details