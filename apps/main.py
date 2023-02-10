from typing import List, Optional
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
async def root() :
    return {"message" : "Hello world!"}

@app.get("/all/")
async def all_movies() :
    return {"message" : "All movies"}

@app.get("/genres/{genres}")
async def genre_movies(genre: str) :
    return {"message" : f"genre: {genre}"}

@app.get("/user-based/")
async def user_based(params: Optional[List[str]] = Query(None)) :
    return {"message" : "user based"}

@app.get("/item-based/{item_id}")
async def item_based(item_id: str):
    return {"message" : f"item based: {item_id}"}