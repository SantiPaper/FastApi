from fastapi import FastAPI
from .routers import movies

app = FastAPI()

app.include_router(movies.router)

@app.get("/")
def home():
    return "Hola FastAPI"
