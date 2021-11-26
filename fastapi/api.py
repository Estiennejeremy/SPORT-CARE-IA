from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from heart import getRmssd
from calcul import stateCalcul, calcul


app = FastAPI()

@app.get("/")
def home():
    return {"data":"Test"}


@app.post("/rmssd")
async def heart(item: list):
    return getRmssd(item)

@app.post("/state")
async def heart(item: list):
    return stateCalcul(item)