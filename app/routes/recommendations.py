# app/routes/recommendations.py
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List
from app.models import Rating, Movie
from app.database import get_session
from app.schemas import MovieRead

router = APIRouter()

@router.get("/{user_id}", response_model=list[MovieRead])
def get_recommendations(user_id: int, session: Session = Depends(get_session)):
    # Obter todos os filmes avaliados pelo usuário
    user_ratings = session.exec(select(Rating).where(Rating.user_id == user_id)).all()
    
    # Obter todos os IDs dos filmes avaliados
    rated_movie_ids = [rating.movie_id for rating in user_ratings]

    # Obter todos os filmes que o usuário ainda não avaliou
    recommended_movies = session.exec(select(Movie).where(Movie.id.notin_(rated_movie_ids))).all()
    
    return recommended_movies
