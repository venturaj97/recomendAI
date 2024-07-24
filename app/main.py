# app/main.py
from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from app.database import init_db
from app.routes import auth, movies, ratings, recommendations
from app.routes.auth import get_current_user

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(movies.router, prefix="/movies", tags=["movies"], dependencies=[Depends(get_current_user)])
app.include_router(ratings.router, prefix="/ratings", tags=["ratings"], dependencies=[Depends(get_current_user)])
app.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"], dependencies=[Depends(get_current_user)])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
