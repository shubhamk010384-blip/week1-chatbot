import requests
import trafilatura
import os

def web_search(query):
    url = "https://google.serper.dev/search"

    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json"
    }

    r = requests.post(
        url,
        headers=headers,
        json={"q": query}
    )

    return r.json().get("organic", [])[:5]


def web_fetch(url):

    html = requests.get(
        url,
        timeout=10
    ).text

    return trafilatura.extract(html) or "No content"
