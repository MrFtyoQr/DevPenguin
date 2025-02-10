# data_access/openrouter_data_access.py
from infrastructure.openrouter_client import OpenRouterClient#aqui importamos la clase OpenRouterClient

class OpenRouterDataAccess:#aqui creamos la clase OpenRouterDataAccess
    def __init__(self):#aqui inicializamos la clase
        self.client = OpenRouterClient()#aqui inicializamos la clase OpenRouterClient
    
    def fetch_response(self, question: str):#aqui creamos el metodo fetch_response que recibe un parametro question question es un string que nosotros proporcionaremos
        return self.client.get_response(question)#aqui retornamos el metodo get_response que se encuentra en la clase OpenRouterClient que recibe un parametro question que es un string que nosotros proporcionaremos