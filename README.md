# AI Chatbot

A conversational AI chatbot built with Python, powered by LLaMA 3 via Groq API.

## Features
- Multi-turn conversation with context memory
- REST API built with FastAPI
- Clean chat UI (HTML/CSS/JS)
- Session-based conversation history

## Tech Stack
- Python
- Groq API (LLaMA 3)
- FastAPI
- Uvicorn

## How to Run
1. Clone the repo
2. Create a virtual environment and install dependencies: pip install groq python-dotenv fastapi uvicorn
3. Create a `.env` file with your Groq API key: GROQ_API_KEY=your-unique-key
4. Run the server: uvicorn api: app --reload
5. Open `http://127.0.0.1:8000` in your browser