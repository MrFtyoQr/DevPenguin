import requests#importamos requests por que sirve para hacer peticiones a una url
import json#importamos json por que sirve para trabajar con archivos json

class OpenRouterClient:#aqui creamos la clase OpenRouterClient
    API_URL = "https://openrouter.ai/api/v1/chat/completions"
    API_KEY = "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"
    #aqui creamos las variables API_URL y API_KEY, API_URL es la url a la que haremos la peticion y API_KEY es la clave que nos permitira hacer la peticion
    def get_response(self, question: str):#aqui creamos el metodo get_response que recibe un parametro question question es un string que nosotros proporcionaremos
        headers = {"Authorization": f"Bearer {self.API_KEY}"}#aqui creamos la variable headers que es un diccionario que contiene la clave Authorization y el valor Bearer mas la clave API_KEY el self se usa para acceder a las variables de la clase
        print("Sending headers:", headers)  # Verifica los encabezados
        response = requests.post(
            url=self.API_URL,
            headers=headers,
            data=json.dumps({
                "model": "google/gemini-2.0-flash-001",
                "messages": [{"role": "user", "content": question}]
            })
        )#aqui creamos la variable response que es la respuesta de la peticion post que se hace a la url API_URL, con los headers y los datos que se envian en el json.dumps
        print(response.status_code)  # Verifica el código de estado
        return response.json()
