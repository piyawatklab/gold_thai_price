from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import db
import models

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/test/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request, 'data': 75}
    return templates.TemplateResponse("item.html", context)


@app.get("/")
async def root():
    return {"message": "test"}


@app.get("/all")
def get_all():
    data = db.all()
    return data


@app.get("/get_current_price_api")
def get_one(date: str):
    data = db.get_one(date)
    return data


@app.get("/get_current_price", response_class=HTMLResponse)
def get_one(request: Request, date="", price_type="ask"):
    data = db.get_one(date)
    context = {'request': request,
               'date': data["date"],
               'price': data["price_"+price_type],
               'price_type': price_type}
    return templates.TemplateResponse("item.html", context)


@app.get("/get_all_by_date/{date}")
def get_by_date(date: str):
    data = db.get_by_date(date)
    return data
