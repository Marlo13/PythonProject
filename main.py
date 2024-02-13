from fastapi import FastAPI, Form, Request, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from jinja2 import Template
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
import json
from pprint import pprint
from typing import Annotated
from pydantic import BaseModel
import os
class LoginForm(BaseModel):
    username: str
    password: str

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Base de données temporaire pour stocker les articles et les commentaires
articles_db = {}
comments_db = {}
if os.path.exists("articles.json"):
    with open("articles.json", mode="r", encoding="utf-8") as file:
        list_articles = json.load(file)
else:
    list_articles = []

utilisateurs = {}
if os.path.exists("users.json"):
    with open("users.json", mode="r", encoding="utf-8") as file:
        list_users = json.load(file)
else:
    list_users = []



###### HOME ######
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
     return templates.TemplateResponse("home.html", {"request": request})





######## Parti connexion ########

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, email: Annotated[str, Form()], password: Annotated[str, Form()]):
    # récupere les données de l'utilisateur de la vue
    utilisateur = {"email": email, "password": password}
    #Verification des identifiants
    with open("users.json", mode="r", encoding="utf-8") as file:
        users = json.load(file)
        for user in users:
            if user["email"] == utilisateur["email"] and user["password"] == utilisateur["password"]:
                return {"message": "Vous êtes connecté"}
    raise HTTPException(status_code=400, detail="Mauvais identifiants")




######## Parti Inscription ########

@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
async def register(request: Request ,name: Annotated[str, Form()], email: Annotated[str, Form()], password: Annotated[str, Form()]):
    # vérifie dans le fichier json users.json si l'utilisateur existe
    utilisateur = {"name": name,"email": email,"password": password}
    for user in list_users:
        if user["email"] == utilisateur["email"]:
            raise HTTPException(status_code=400, detail="Cet utilisateur existe déjà")
    #ajoute l'utilisateur dans la liste
    list_users.append(utilisateur)
    # Ajouter l'utilisateur dans le fichier JSON
    with open("users.json", mode="w", encoding="utf-8") as file:
        json.dump(list_users, file, indent=4)
    return {"message": "Utilisateur créé avec succès"}



##### Profil #####
@app.get("/profil", response_class=HTMLResponse)
async def profil(request: Request):
    return templates.TemplateResponse("profil.html", {"request": request}, {"list_users": list_users})



######## Parti articles ########
# Route pour afficher la liste des articles
@app.get("/articles", response_class=HTMLResponse)
async def articles(request: Request):
    return templates.TemplateResponse("articles.html", {"request": request, "list_articles": list_articles})

# Route pour afficher le formulaire de création d'article
@app.get("/create_article", response_class=HTMLResponse)
async def create_article(request: Request):
    return templates.TemplateResponse("create_article.html", {"request": request})

# Route pour créer un nouvel article
@app.post("/create_article")
async def create_article(title: Annotated[str, Form()], content: Annotated[str, Form()]):
    articles_db = {"title": title, "content": content}
    list_articles.append(articles_db)
    # Ajouter l'article dans le fichier JSON
    with open("articles.json", mode="w", encoding="utf-8") as file:
        json.dump(list_articles, file, indent=4)
    return {"message": "Article créé avec succès"}

# editer un article
@app.get("/edit_article/{article_id}", response_class=HTMLResponse)
async def edit_article(request: Request, article_id: int):
    article = list_articles[article_id]
    return templates.TemplateResponse("edit_article.html", {"request": request, "article": article, "article_id": article_id})

@app.post("/edit_article/{article_id}")
async def edit_article(request: Request, article_id: int, title: Annotated[str, Form()], content: Annotated[str, Form()]):
    list_articles[article_id] = {"title": title, "content": content}
    # Ajouter l'article dans le fichier JSON
    with open("articles.json", mode="w", encoding="utf-8") as file:
        json.dump(list_articles, file, indent=4)
    return {"message": "Article modifié avec succès"}


if __name__ == "__main__":
   uvicorn.run("main:app", host="localhost", port=3000, reload=True)