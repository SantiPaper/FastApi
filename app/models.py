from pydantic import BaseModel, Field
import datetime

class Movie(BaseModel):
    id: int
    title: str
    year: int
    category: str

class MovieUpdate(BaseModel):
    title: str
    year: int
    category: str

class MovieCreate(BaseModel):
    id: int
    title: str = Field(min_length=2, max_length=20)
    year: int = Field(le=datetime.date.today().year, ge=1900)
    category: str = Field(min_length=2, max_length=20, default="None")
