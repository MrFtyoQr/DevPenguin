# infra.py
import requests
from typing import Optional
from models.pokemon_models import PokemonResponse

class PokemonInfra:
    def get_pokemon_info(self, name: str) -> Optional[PokemonResponse]:
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            types = [t['type']['name'] for t in data['types']]
            abilities = [a['ability']['name'] for a in data['abilities']]
            
            return PokemonResponse(
                name=data['name'],
                height=data['height'],
                weight=data['weight'],
                types=types,
                abilities=abilities
            )
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                return None
            raise