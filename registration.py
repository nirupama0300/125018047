from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import requests

app = FastAPI()

class Register(BaseModel):
    class Register(BaseModel):
        companyName: str
        ownerName: str
        rollNo: int
        ownerEmail: str
        accessCode: str


@app.post("/register")
def register(register:Register):
    url = "https://20.244.56.144/test/register"
    payload = register.dict()
    headers = {
        "Content - Type":"application/json"
    }