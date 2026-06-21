import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "llama3"

MOCK_RESPONSE = """You are a highly capable AI assistant. 

Task: {task}

Please complete this task following these guidelines:
- Be clear, structured, and precise in your response
- Follow any constraints or formatting requirements mentioned above
- Adapt your tone and depth to match the intended audience
- Prioritize accuracy and completeness over brevity

Respond in a well-organized format appropriate to the task."""

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
