

import requests
import json

# Solicitar la pregunta desde la terminal
pregunta = input("Por favor, ingrese su pregunta: ")

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer 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"
    },
    data=json.dumps({
        "model": "google/gemini-2.0-flash-001",
        "messages": [
            {
                "role": "user", "content": pregunta }
        ]
    })
)

print(response.json())