import requests

class PokemonService:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/pokemon"

    def get_pokemon(self, pokemon):
        response = requests.get(f"{self.base_url}/{pokemon}")

        if response.status_code != 200:
            return {"error": f"HTTP error: {response.status_code}"}

        data = response.json()

        # Filtrar los datos relevantes
        pokemon_info = {
            "Nombre": data.get("name"),
            "Altura": data.get("height"),
            "Experiencia Base": data.get("base_experience"),
            "Habilidades": [ability["ability"]["name"] for ability in data.get("abilities", [])],
            "Movimientos": [move["move"]["name"] for move in data.get("moves", [])[:5]],  # Solo 5 movimientos como ejemplo
        }

        return pokemon_info