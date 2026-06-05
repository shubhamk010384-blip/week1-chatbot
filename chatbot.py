import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Add it to .env file")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

chat_history = [
    {
        "role": "user",
        "parts": ["You are a helpful AI chatbot. Keep memory of the conversation."]
    }
]

print("🤖 Week 1 Chatbot (type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye! 👋")
        break

    chat_history.append({
        "role": "user",
        "parts": [user_input]
    })

    response = model.generate_content(chat_history)
    bot_reply = response.text

    print("Bot:", bot_reply)

    chat_history.append({
        "role": "model",
        "parts": [bot_reply]
    })