# dal.py
from infrastructure.pokemon_infra import PokemonInfra
from models.pokemon_models import PokemonResponse

class PokemonDAL:
    def __init__(self):
        self.infra = PokemonInfra()
    
    def fetch_pokemon_data(self, name: str) -> PokemonResponse:
        result = self.infra.get_pokemon_info(name)
        if not result:
            raise ValueError("Pokemon no encontrado")
        return result