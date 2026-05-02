from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import get_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

sessions = {}

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.get("/")
def home():
    return FileResponse("templates/index.html")

@app.post("/chat")
def chat(req: ChatRequest):
    if req.session_id not in sessions:
        sessions[req.session_id] = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

    history = sessions[req.session_id]
    history.append({"role": "user", "content": req.message})

    reply = get_response(history)
    history.append({"role": "assistant", "content": reply})

    return {"reply": reply, "session_id": req.session_id}