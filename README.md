AI Knowledge Hub

A fullstack AI-powered web application to ask questions based on your own text.
Built with FastAPI (backend) and React (frontend). Uses OpenAI API for AI responses.

Features

- Paste any text and ask questions about it.
- AI provides answers using the provided text.
- Mock fallback answers for local testing without API key.
- Responsive and clean UI.

Tech Stack

Backend: FastAPI, Python, Pydantic
Frontend: React.js, HTML, CSS, JavaScript
Database: MongoDB (optional, for storing documents)
AI: OpenAI API (mock answers for free use)
Tools: VS Code, Git, Postman

Installation & Setup (Local)

1. Clone the backend repo
git clone https://github.com/Bharath-world/ai-knowledge-hub-backend.git
cd ai-knowledge-hub-backend

2. Create virtual environment and install dependencies
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

3. Run backend
python -m uvicorn main:app --reload

4. Run frontend (from your React project folder)
npm install
npm start

Usage

1. Open the frontend in your browser (http://localhost:3000)
2. Paste your text in the input box
3. Ask a question related to the text
4. Get AI-generated answers instantly

Notes

OpenAI API key is required for real AI responses. For free usage, mock answers are used.
Ensure .env is added to .gitignore to keep secrets safe.

Author

Bharath Chandra
GitHub: https://github.com/Bharath-world

