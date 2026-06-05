# Week 1 Chatbot – CSOT26 GenAI Agentic

A terminal-based chatbot using Gemini API with:
- Multi-turn conversation memory
- Secure API key using `.env`
- CLI interaction
- GitHub-ready structure

## Project Structure

```txt
week1-chatbot/
│── chatbot.py
│── requirements.txt
│── .env.example
│── .gitignore
│── README.md
```

## Setup

### 1. Clone Repo
```bash
git clone <your-repo-url>
cd week1-chatbot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add API Key
Rename `.env.example` to `.env` and add:

```env
GEMINI_API_KEY=your_api_key_here
```

Get a Gemini API key from Google AI Studio.

### 4. Run Chatbot
```bash
python chatbot.py
```

Example:
```txt
You: Hi
Bot: Hello!

You: My name is Shubham
Bot: Nice to meet you, Shubham!

You: What is my name?
Bot: Your name is Shubham.
```