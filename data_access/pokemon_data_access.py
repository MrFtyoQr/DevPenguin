class PokemonDataAccess:
    def __init__(self, pokemon_service):
        self.pokemon_service = pokemon_service

    def fetch_pokemon(self, pokemon: str) -> str: # del tipo pokemon no
        print("recibimos request de business haremos el request a la infraestructura")
        
        pokemon = self.pokemon_service.get_pokemon(pokemon)
        print(pokemon)
        return pokemon