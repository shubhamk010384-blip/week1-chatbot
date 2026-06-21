import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")


client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)
MODELS = {
    "1": "meta-llama/llama-3.1-8b-instruct:free",
    "2": "deepseek/deepseek-r1-0528:free"
}

print("Choose Model")
print("1. Llama 3.1")
print("2. DeepSeek")

choice = input("Enter choice: ")

selected_model = MODELS.get(choice)

if selected_model is None:
    print("Invalid choice")
    exit()


chat_history = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

print("🤖 Week 1 Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye! 👋")
        break

    
    chat_history.append({
        "role": "user",
        "content": user_input
    })

    
    response = client.chat.completions.create(
        model=selected_model,
        messages=chat_history
    )

    bot_reply = response.choices[0].message.content

    print("Bot:", bot_reply)

    # Save bot response
    chat_history.append({
        "role": "assistant",
        "content": bot_reply
    })
