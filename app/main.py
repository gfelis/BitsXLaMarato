from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import pomegranate as pm

app = FastAPI() 


class Pacient(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


def prediction(Pacient: pacient):
    pm.BayesianNetwork.from_json("model.txt")

@app.get("/predit/")
async def predict(Pacient: pacient):
    return prediction(pacient)