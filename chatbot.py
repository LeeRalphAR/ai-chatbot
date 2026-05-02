import os
from groq import Groq

# Manually read .env file
env_path = os.path.join(os.path.dirname(__file__), '.env')
with open(env_path) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            key, value = line.split('=', 1)
            os.environ[key.strip()] = value.strip()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_response(messages: list) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    return response.choices[0].message.content

def run_chatbot():
    print("AI Chatbot is running! Type 'quit' to exit.\n")

    conversation = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        conversation.append({"role": "user", "content": user_input})
        reply = get_response(conversation)
        conversation.append({"role": "assistant", "content": reply})

        print(f"Bot: {reply}\n")

if __name__ == "__main__":
    run_chatbot()