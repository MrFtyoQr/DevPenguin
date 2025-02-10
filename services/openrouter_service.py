# services/openrouter_service.py
from data_access.openrouter_data_access import OpenRouterDataAccess#aqui importamos la clase OpenRouterDataAccess

class OpenRouterService:#aqui creamos la clase OpenRouterService
    def __init__(self):#aqui inicializamos la clase
        self.data_access = OpenRouterDataAccess()#aqui inicializamos la clase OpenRouterDataAccess, mas exactamente el metodo fetch_response que sirve para obtener la respuesta
    
    def get_response(self, question: str):#aqui creamos el metodo get_response que recibe un parametro question question es un string que nosotros proporcionaremos
        return self.data_access.fetch_response(question)#aqui retornamos el metodo fetch_response que se encuentra en la clase OpenRouterDataAccess que recibe un parametro question que es un string que nosotros proporcionaremos