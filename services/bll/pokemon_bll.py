# bll.py
from data_access.dal.pokemon_dal import PokemonDAL
from models.pokemon_models import PokemonResponse

class PokemonBLL:
    def __init__(self):
        self.dal = PokemonDAL()
    
    def get_pokemon_data(self, name: str) -> PokemonResponse:
        return self.dal.fetch_pokemon_data(name)