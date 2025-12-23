🧠 Text to Durable Rules Generator

An AI-powered system that converts natural language policy text into executable Durable Rules using LLMs, FastAPI, and Streamlit.

This project demonstrates how Large Language Models can be safely integrated with deterministic rule engines for real-world use cases like insurance, finance, and compliance systems.

🚀 Features

Convert plain English rules into structured JSON

Generate Python Durable Rules automatically

Clean separation of:

AI reasoning (LLM)

Business logic (rule engine)

REST API backend using FastAPI

Interactive frontend using Streamlit

Secure API key handling with environment variables

🏗️ Architecture Overview
User
 │
 ▼
Streamlit Frontend
 │  (HTTP Request)
 ▼
FastAPI Backend
 │
 ├─ LLM (Text → JSON)
 │
 ├─ JSON Validation
 │
 └─ Durable Rules Generator
 │
 ▼
Generated Rule Output

📁 Project Structure
text-to-durable-rules/
│
├── backend/
│   ├── app.py                # FastAPI application
│   ├── llm_service.py        # LLM integration
│   ├── rule_generator.py     # JSON → Durable Rules
│   ├── rules/
│   │   └── generated_rules.py
│   ├── .env                  # API key (not committed)
│   ├── requirements.txt
│
├── frontend/
│   ├── app.py                # Streamlit UI
│   └── requirements.txt
│
└── README.md

🛠️ Tech Stack

Python 3.10+

FastAPI – Backend API

Streamlit – Frontend UI

OpenAI API – LLM for text understanding

Durable Rules – Rule engine

Uvicorn – ASGI server

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/text-to-durable-rules.git
cd text-to-durable-rules

2️⃣ Backend Setup
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Create a .env file:

OPENAI_API_KEY=sk-your-api-key-here


⚠️ Use a standard sk- key, not sk-or-v1

Run backend:

uvicorn app:app --reload


Open Swagger UI:

http://127.0.0.1:8000/docs

3️⃣ Frontend Setup

Open a new terminal:

cd frontend
pip install -r requirements.txt
streamlit run app.py


The app will open automatically in your browser.

🧪 Example Usage
Input
If vehicle age is greater than 10 and accident count is more than 2 then reject the insurance

Output

Structured JSON representation

Executable Durable Rules Python code

🧠 Why This Project Matters

Demonstrates LLM + backend engineering

Handles probabilistic AI output safely

Real-world applicable (InsurTech, FinTech, Compliance)

Resume-worthy architecture

Production-style error handling

🧩 Future Enhancements

Rule execution testing (input facts → decision)

Rule versioning and persistence

Multiple rule sets support

User authentication

Deployment (AWS / Render / HuggingFace)

🔒 Security Notes

API keys are stored in .env

.env is excluded via .gitignore

Backend-only access to LLM
