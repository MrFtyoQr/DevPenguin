# data_access/openrouter_data_access.py
from infrastructure.openrouter_client import OpenRouterClient

class OpenRouterDataAccess:
    def __init__(self):
        self.client = OpenRouterClient()
    
    def fetch_response(self, question: str):
        return self.client.get_response(question)