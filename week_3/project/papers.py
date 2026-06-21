import requests

def paper_search(query):

    url = "https://huggingface.co/api/papers/search"

    try:
        r = requests.get(
            url,
            params={"q": query},
            timeout=15
        )

        return r.json()

    except Exception as e:
        return {"error": str(e)}


def read_paper(arxiv_id):

    return {
        "message":
        f"Paper reader placeholder for {arxiv_id}"
    }
