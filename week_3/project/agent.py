import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from tools.web import web_search, web_fetch
from tools.files import read_file, write_file, list_files
from tools.papers import paper_search, read_paper

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


class Agent:

    def __init__(self, session_id="default"):

        self.session_id = session_id

        self.messages = [
            {
                "role": "system",
                "content": (
                    "You are Research Desk. "
                    "You can use web search, paper search, "
                    "and file tools to help with research."
                )
            }
        ]

        self.load_session()

    def session_path(self):

        os.makedirs(
            "sessions",
            exist_ok=True
        )

        return f"sessions/{self.session_id}.json"

    def save_session(self):

        with open(
            self.session_path(),
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.messages,
                f,
                indent=2
            )

    def load_session(self):

        try:
            with open(
                self.session_path(),
                "r",
                encoding="utf-8"
            ) as f:

                self.messages = json.load(f)

        except FileNotFoundError:
            pass

    def run(self, query):

        self.messages.append(
            {
                "role": "user",
                "content": query
            }
        )

        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=self.messages
        )

        reply = response.choices[0].message.content

        self.messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

        self.save_session()

        return reply


class REPLAgent(Agent):

    def run_loop(self):

        print("🔬 Week 3 Research Desk")
        print("Type 'exit' to quit.\n")

        while True:

            q = input("You: ")

            if q.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            print("Bot:", self.run(q))


if __name__ == "__main__":

    agent = REPLAgent()

    agent.run_loop()
