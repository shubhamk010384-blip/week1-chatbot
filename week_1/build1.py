import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

prompt = input("Prompt: ")

response = client.chat.completions.create(
    model="meta-llama/llama-3.1-8b-instruct:free",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(response)
