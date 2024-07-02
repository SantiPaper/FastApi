from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Movie, MovieUpdate, MovieCreate
from ..database import movies

router = APIRouter(
    prefix="/movies",
    tags=["movies"]
)

@router.get("/", response_model=List[Movie])
def get_movies():
    return movies

@router.get("/{id}", response_model=Movie)
def get_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

@router.get("/category/", response_model=List[Movie])
def get_movie_by_category(category: str):
    arr = [movie for movie in movies if movie["category"].lower() == category.lower()]
    if arr:
        return arr
    raise HTTPException(status_code=404, detail="There are no movies in this category.")

@router.post("/", response_model=List[Movie])
def create_movie(movie: MovieCreate):
    movies.append(movie.dict())
    return movies

@router.delete("/{id}", response_model=dict)
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return {"message": f"{movie['title']} has been deleted"}
    raise HTTPException(status_code=404, detail="Movie not found")

@router.put("/{id}", response_model=MovieUpdate)
def update_movie(id: int, movie: MovieUpdate):
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["year"] = movie.year
            item["category"] = movie.category
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")
