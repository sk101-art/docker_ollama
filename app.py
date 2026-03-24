import requests
import os

# Use the Docker service name 'ollama-engine'
OLLAMA_URL = os.getenv("OLLAMA_HOST", "http://ollama-engine:11434") + "/api/generate"

def chat():
    print("\n--- Live AI Terminal (Type 'exit' to quit) ---")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break

        payload = {
            "model": "llama3.2:1b",
            "prompt": user_input,
            "stream": False
        }

        try:
            response = requests.post(OLLAMA_URL, json=payload)
            response.raise_for_status()
            print(f"AI: {response.json()['response']}\n")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat()