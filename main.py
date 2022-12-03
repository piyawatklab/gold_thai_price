from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import db
import models

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return {"message": "test"}

@app.get("/all")
def get_all():
    data = db.all()
    return {"data": data}

@app.get("/get/{date}")
def get_one(date:str):
    data = db.get_one(date)
    return {"data": data}

@app.get("/get_by_date/{date}")
def get_by_date(date:str):
    data = db.get_by_date(date)
    return {"data": data}