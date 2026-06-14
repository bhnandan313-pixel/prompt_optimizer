import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "llama3"

MOCK_RESPONSE = """Enhanced Prompt:
You are a helpful assistant. Your task is to complete the given objective
clearly and precisely based on the provided constraints and preferences."""

def enhance_prompt(assembled_prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": assembled_prompt,
                "system": "You are a prompt engineering expert. Rewrite the given prompt into a clear, structured, high-quality version based on the user preferences provided.",
                "stream": False
            },
            timeout=30
        )

        data = response.json()
        return data.get("response", MOCK_RESPONSE)

    except Exception as e:
        return f"[OFFLINE MODE]\n{MOCK_RESPONSE}\n\n(Ollama not running: {str(e)})"
