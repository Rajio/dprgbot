import httpx
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Ми можемо вибрати модель, наприклад цю:
MODEL_NAME = "meta-llama/llama-4-scout-17b-16e-instruct"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

async def generate_alternative(field_value: str, prompt: str):
    async with httpx.AsyncClient() as client:
        data = {
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": "You are an assistant for rewriting podcast data."},
                {"role": "user", "content": f"{prompt}\n\nOriginal: {field_value}"}
            ]
        }
        response = await client.post(GROQ_API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
