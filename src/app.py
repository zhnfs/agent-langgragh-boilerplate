from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI(title="LangGraph Agent API")

@app.get("/")
def read_root():
    return {"message": "LangGraph Agent is running!"}

# Example: expose your agent as an endpoint
from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(model="gemma-4-31b-it")

from pydantic import BaseModel

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(request: ChatRequest):
    response = model.invoke(request.prompt)
    return {"response": response}
