class PokemonBLL:
    def __init__(self, pokemon_data_access):
        self.pokemon_data_access = pokemon_data_access

    def get_pokemon(self, pokemon: str) -> str:
        print("el enrutador nos mando al business y vamos a mandar llamar al data access")
        pokemon = self.pokemon_data_access.fetch_pokemon(pokemon)
        print(pokemon)
        return pokemon