from fastapi import FastAPI, status
from starlette.responses import Response, JSONResponse
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

players_db = []

class Player(BaseModel):
    Number: int
    Name: str

@app.get("/")
def read_root():
    return {"Message": "It's just the root"}

@app.get("/hello")
def hello():
    with open("hello.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    return Response(
        content=html_content,
        status_code=200,
        media_type="text/html"
    )
@app.get("/welcome")
def welcome(name: str):
    message = f"Welcome {name}"
    return JSONResponse(content={"message": message}, status_code=200)

@app.post("/players", status_code=status.HTTP_201_CREATED)
def add_players(players: List[Player]):
    players_db.extend(players)
    return players_db

@app.get("/players", status_code=status.HTTP_200_OK)
def get_players():
    return players_db

@app.put("/players", status_code=status.HTTP_200_OK)
def put_player(player: Player):
    for i, existing_player in enumerate(players_db):
        if existing_player.Number == player.Number:
            if existing_player != player:
                players_db[i] = player
            return players_db
    players_db.append(player)
    return players_db