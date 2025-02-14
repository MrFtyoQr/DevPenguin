# models.py
from pydantic import BaseModel
from typing import List

class PokemonResponse(BaseModel):
    name: str
    height: int
    weight: int
    types: List[str]
    abilities: List[str]