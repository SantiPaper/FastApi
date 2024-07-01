from fastapi import FastAPI, Body


app = FastAPI()

app.title = "Mi primera app con fastApi"

""" Tags: tags=["soy un tag"] """

movies = [{
  "id": 1,
  "title":"Avatar",
  "year": "2009",
  "category":"tccion"
},
{
  "id": 2,
  "title":"Boruto",
  "year": "2020",
  "category":"tccion"
},
{
  "id": 3,
  "title":"X",
  "year": "2009",
  "category":"terror"
}]

@app.get("/")
def home():
  return "Hola fastApi"

@app.get("/movies")
def get_movies():
  return movies

@app.get("/movies/{id}")
def get_movie(id: int):
  for movie in movies:
    if movie["id"] == id:
     return movie
  return "Movie not found"

@app.get("/movies/")
def get_movie_by_category(category: str):
  arr = []
  for movie in movies:
    if movie["category"] == category.lower():
      arr.append(movie)
  if len(arr) > 0: return arr
  return "There are no movies in this category."



@app.post("/movies")
def create_movie(id:int = Body(),title:str = Body(),year:int = Body(),category:str = Body()):
  movies.append({
    "id": id,
    "title": title,
    "year":year,
    "category":category
  })
  return movies

@app.delete("/movies/{id}")
def delete_movie(id:int):
  for movie in movies:
    if movie["id"] == id:
       movies.remove(movie)
       return {"message": f"{movie['title']} has been deleted"}
  return movies

@app.put("/movies/{id}")
def update_movie(id:int,title : str = Body(), year : int = Body(),category : str = Body()):

  for movie in movies:
    if movie["id"] == id:
      movie["title"] = title
      movie["year"] = year
      movie["category"] = category
  return movie   

    