# app/tmdb_client.py
import httpx
from typing import List

API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZWY0YmM3M2JjZmIzZTc1ZjQ3MjBhNWM0ZmNlNTI1NyIsIm5iZiI6MTcyMTg0MDA1NC44ODg1MDgsInN1YiI6IjY2YTEzMTIxNGVlN2Y5ZjBlZGRkN2ExNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zSoRmLfMAgiJKrhIcLVjMzmTZ-J-2aANUaB4CVm4uPc"
BASE_URL = "https://api.themoviedb.org/3ef4bc73bcfb3e75f4720a5c4fce5257"

async def fetch_movie_details(movie_id: int) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/movie/{movie_id}", params={"api_key": API_KEY})
        response.raise_for_status()
        return response.json()

async def search_movies(query: str) -> List[dict]:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/search/movie", params={"api_key": API_KEY, "query": query})
        response.raise_for_status()
        return response.json().get("results", [])
