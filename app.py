from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api.pokemon_router import pokemon_router
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI()
app.include_router(pokemon_router, prefix="/api")

# Serve static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.get("/history")
async def read_history():
    return templates.TemplateResponse("history.html", {"request": {}})