from openai import OpenAI
from dotenv import load_dotenv
import os
from tools import web_search, web_fetch
load_dotenv()

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

SYSTEM_PROMPT = """You are a research agent. Use tools for research.
Available tools:
1. web_search(query)
2. web_fetch(url)
Research step-by-step and synthesize answers.
"""

def ask_agent(query, log=None):
    msgs=[{"role":"system","content":SYSTEM_PROMPT},{"role":"user","content":query}]
    resp=client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=msgs
    )
    if log: log("LLM response generated")
    return resp.choices[0].message.content
