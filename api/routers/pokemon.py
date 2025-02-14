# routers/pokemon.py
from fastapi import APIRouter, HTTPException
from services.bll.pokemon_bll import PokemonBLL
from models.pokemon_models import PokemonResponse

router = APIRouter(prefix="/api/pokemon", tags=["Pokemon"])
bll = PokemonBLL()

@router.get("/{name}", response_model=PokemonResponse)
async def get_pokemon(name: str):
    try:
        return bll.get_pokemon_data(name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")