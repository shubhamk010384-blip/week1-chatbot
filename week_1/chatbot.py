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
class ChatAgent:

    def __init__(
        self,
        model,
        system_prompt,
        max_history_turns=10
    ):
        self.model = model
        self.max_history_turns = max_history_turns

        self.chat_history = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

    def trim_history(self):

        max_messages = self.max_history_turns * 2 + 1

        if len(self.chat_history) > max_messages:
            self.chat_history = (
                self.chat_history[:1]
                + self.chat_history[-(max_messages - 1):]
            )

    def chat(self, user_input):

        self.chat_history.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        self.trim_history()

        response = client.chat.completions.create(
            model=self.model,
            messages=self.chat_history
        )

        reply = response.choices[0].message.content

        self.chat_history.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

        return reply


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


agent = ChatAgent(
    model=selected_model,
    system_prompt="You are a helpful AI assistant.",
    max_history_turns=10
)

print("🤖 Week 1 Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit","quit"]:
        print("Bot: Goodbye! 👋")
        break

    bot_reply = agent.chat(user_input)

    print("Bot:", bot_reply)
   

  
