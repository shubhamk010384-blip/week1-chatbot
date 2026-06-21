import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


class Agent:

    def __init__(
        self,
        session_id="default"
    ):

        self.session_id = session_id

        self.messages = [
            {
                "role": "system",
                "content":
                "You are Research Desk."
            }
        ]

        self.load_session()

    def session_path(self):

    os.makedirs(
        "sessions",
        exist_ok=True
    )

    return (
        f"sessions/{self.session_id}.json"
    )

    def save_session(self):

        with open(
            self.session_path(),
            "w"
        ) as f:
            json.dump(
                self.messages,
                f
            )

    def load_session(self):

        try:
            with open(
                self.session_path(),
                "r"
            ) as f:

                self.messages = json.load(f)

        except:
            pass

    def run(self, query):

        self.messages.append(
            {
                "role": "user",
                "content": query
            }
        )

        response = (
            client.chat.completions.create(
                model="openai/gpt-4o-mini",
                messages=self.messages
            )
        )

        reply = (
            response
            .choices[0]
            .message
            .content
        )

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

        while True:

            q = input("You: ")

            if q.lower() in [
                "exit",
                "quit"
            ]:
                break

            print(
                self.run(q)
            )


if __name__ == "__main__":

    agent = REPLAgent()

    agent.run_loop()
