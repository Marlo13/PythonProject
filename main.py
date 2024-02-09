from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from jinja2 import Template
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
import json


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root():
    return {"Bye": "Man"}


@app.get("/template1", response_class=HTMLResponse)
async def read_template1(request: Request):
    return templates.TemplateResponse(
        request=request, name="template1.html")


def count_occurence(list1):
    list2 = {}
    list1 = list1.split(" ")
    for x in list1:
        list2[x] = f" apparait {list1.count(x)} fois"
    formated_list =  list2
    #formated_list = json.dumps(list2, indent=1)
    return formated_list


@app.post("/post_form")
async def post_form(request: Request):
    form_data = await request.form()
    result = count_occurence(form_data["textarea1"])

    return {"Message": result}




if __name__ == "__main__":
   uvicorn.run("main:app", host="localhost", port=3000, reload=True)