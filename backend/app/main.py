from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routes import auth, mood, stats
from backend.app import models, database

app = FastAPI(title="Mood Diary API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(mood.router, prefix="/mood")
app.include_router(stats.router, prefix="/stats")

@app.get("/")
def read_root():
    return {"msg": "Welcome to Mood Diary API"}

# Create tables
models.Base.metadata.create_all(bind=database.engine)
