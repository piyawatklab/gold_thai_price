from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import db
import models

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/test")
def root():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/")
async def root():
    return {"message": "test"}

@app.get("/all")
def get_all():
    data = db.all()
    return data


@app.get("/get_current_price")
def get_one(date: str):
    data = db.get_one(date)
    return data
# def get_last():
#     data = db.get_last()
#     return {"data": data}


@app.get("/get_all_by_date/{date}")
def get_by_date(date: str):
    data = db.get_by_date(date)
    return data
