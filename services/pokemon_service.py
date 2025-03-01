import requests
from data_access.coach_db import CoachDB

class PokemonService:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/pokemon"
        self.db = CoachDB()

    def get_pokemon(self, pokemon):
        response = requests.get(f"{self.base_url}/{pokemon}")

        if response.status_code != 200:
            return {"error": f"HTTP error: {response.status_code}"}

        data = response.json()

        # Filtrar los datos relevantes
        pokemon_info = {
            "name": data.get("name"),
            "height": data.get("height"),
            "weight": data.get("weight"),
            "types": ", ".join([t["type"]["name"] for t in data.get("types", [])]),
            "abilities": ", ".join([a["ability"]["name"] for a in data.get("abilities", [])])
        }

        # Save to history automatically
        self.db.save_history(pokemon_info)

        return pokemon_info

    def save_pokemon(self, pokemon_info):
        self.db.save_pokemon(pokemon_info)

    def get_saved_pokemon(self):
        return self.db.get_saved_pokemon()

    def get_history(self):
        return self.db.get_history()
