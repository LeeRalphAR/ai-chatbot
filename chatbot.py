import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key="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")

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