
import os
import requests

API_KEY = os.getenv("OPENAI_API_KEY")
API_ENDPOINT = os.getenv("OPENAI_ENDPOINT")

def query_model(prompt: str) -> str:
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY,
    }
    payload = {
        "messages": [
            {"role": "system", "content": "You are OfficeKing, an expert Microsoft Office assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post(API_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"
