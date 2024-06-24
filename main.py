from fastapi import FastAPI

app = FastAPI()

app.title = "Mi primera app con fastApi"

""" Tags: tags=["soy un tag"] """

libros = [{
  "nombre":"hola",
  "apellido":"apellido",
  "author":"Pepe"
},
{
  "nombre":"hola",
  "apellido":"apellido",
  "author":"Pepe"
},
{
  "nombre":"hola",
  "apellido":"apellido",
  "author":"Pepe"
}]

@app.get("/")
def home():
  return "Hola fastApi"

@app.get("/libros")
def home():
  return libros
