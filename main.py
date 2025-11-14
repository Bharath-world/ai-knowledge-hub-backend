from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load OpenAI key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Local storage (no MongoDB needed)
history = []

class Query(BaseModel):
    text: str
    question: str

@app.post("/ask")
async def ask(query: Query):
    # Use OpenAI for real AI answers
    response = openai.ChatCompletion.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": f"Text:\n{query.text}\nQuestion: {query.question}"}]
    )
    answer = response.choices[0].message.content

    # Save to local history
    history.append({"text": query.text, "question": query.question, "answer": answer})

    return {"answer": answer}

@app.get("/history")
async def get_history():
    return history

@app.get("/")
def home():
    return {"message": "Server is working!"}
