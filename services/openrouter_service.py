# services/openrouter_service.py
from data_access.openrouter_data_access import OpenRouterDataAccess

class OpenRouterService:
    def __init__(self):
        self.data_access = OpenRouterDataAccess()
    
    def get_response(self, question: str):
        return self.data_access.fetch_response(question)