from data_access.pokemon_data_access import PokemonDataAccess
from fastapi import APIRouter, HTTPException
from infrastructure.pokemon_service import PokemonService
from services.pokemon_bll import PokemonBLL

pokemon_router = APIRouter()

pokemon_service = PokemonService()
pokemon_data_access = PokemonDataAccess(pokemon_service=pokemon_service)
pokemon_bll = PokemonBLL(pokemon_data_access=pokemon_data_access)

@pokemon_router.get("/{pokemon}")
async def get_pokemon(pokemon: str):
    try:
        print("aqui entro al enrutador de pokemon")
        print("ruta: /" + pokemon)
        return pokemon_bll.get_pokemon(pokemon)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@pokemon_router.post("/save")
async def save_pokemon(pokemon_info: dict):
    try:
        pokemon_service.save_pokemon(pokemon_info)
        return {"message": "Pokemon saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@pokemon_router.get("/saved")
async def get_saved_pokemon():
    try:
        return pokemon_service.get_saved_pokemon()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@pokemon_router.get("/history")
async def get_history():
    try:
        return pokemon_service.get_history()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))