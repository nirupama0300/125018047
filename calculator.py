from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class data(BaseModel):
    windowPrevState : int
    windowCurrentSTate: int
    numbers : int
    avg : int

class average_calculator(info:data):
    try:
    calculate()
