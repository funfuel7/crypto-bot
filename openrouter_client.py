import requests
from config import OPENROUTER_API_KEY


BASE = 'https://openrouter.ai/api/v1'


def ask_openrouter(prompt: str, model: str = 'gpt-4o-mini') -> str:
"""Send a short prompt to OpenRouter and return assistant's reply text.
We use the response as advisory input for the trader.
"""
headers = {'Authorization': f'Bearer {OPENROUTER_API_KEY}', 'Content-Type': 'application/json'}
payload = {
'model': model,
'messages': [
{'role': 'system', 'content': 'You are a world-class crypto scalper analyst and risk manager.'},
{'role': 'user', 'content': prompt}
],
'max_tokens': 300,
'temperature': 0.1,
}
r = requests.post(f'{BASE}/chat/completions', json=payload, headers=headers, timeout=20)
r.raise_for_status()
data = r.json()
# openrouter returns choices similar to OpenAI
return data['choices'][0]['message']['content']
