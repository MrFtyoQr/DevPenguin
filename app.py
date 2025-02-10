from fastapi import FastAPI
from api.routers import router
from api.pokemon_router import pokemon_router
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI()
app.include_router(router, prefix="/api")
app.include_router(pokemon_router, prefix="/pokemon")