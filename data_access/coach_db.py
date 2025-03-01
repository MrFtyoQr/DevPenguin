import requests
from typing import List, Dict

class CoachDB:
    def __init__(self, db_url: str = "http://127.0.0.1:5984", user: str = "joseph", password: str = "54321"):
        self.db_url = db_url
        self.auth = (user, password)
        self.pokemon_db = "crud-pokemon"
        self.history_db = "historico-crud"

    def save_pokemon(self, pokemon: Dict):
        response = requests.post(f"{self.db_url}/{self.pokemon_db}", json=pokemon, auth=self.auth)
        if response.status_code not in [200, 201]:
            print(f"Failed to save pokemon: {response.text}")

    def save_history(self, pokemon: Dict):
        response = requests.post(f"{self.db_url}/{self.history_db}", json=pokemon, auth=self.auth)
        if response.status_code not in [200, 201]:
            print(f"Failed to save history: {response.text}")

    def get_saved_pokemon(self) -> List[Dict]:
        response = requests.get(f"{self.db_url}/{self.pokemon_db}/_all_docs?include_docs=true", auth=self.auth)
        if response.status_code == 200:
            docs = response.json().get("rows", [])
            return [doc["doc"] for doc in docs]
        else:
            print(f"Failed to get saved pokemon: {response.text}")
            return []

    def get_history(self) -> List[Dict]:
        response = requests.get(f"{self.db_url}/{self.history_db}/_all_docs?include_docs=true", auth=self.auth)
        if response.status_code == 200:
            docs = response.json().get("rows", [])
            return [doc["doc"] for doc in docs]
        else:
            print(f"Failed to get history: {response.text}")
            return []
