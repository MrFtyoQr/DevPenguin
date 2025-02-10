import requests
import json

class OpenRouterClient:
    API_URL = "https://openrouter.ai/api/v1/chat/completions"
    API_KEY = "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"
    
    def get_response(self, question: str):
        headers = {"Authorization": f"Bearer {self.API_KEY}"}
        print("Sending headers:", headers)  # Verifica los encabezados
        response = requests.post(
            url=self.API_URL,
            headers=headers,
            data=json.dumps({
                "model": "google/gemini-2.0-flash-001",
                "messages": [{"role": "user", "content": question}]
            })
        )
        print(response.status_code)  # Verifica el código de estado
        return response.json()
