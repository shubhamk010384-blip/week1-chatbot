from pathlib import Path

def list_files(path="."):

    p = Path(path)

    if not p.exists():
        return {"error": "path not found"}

    return {
        "files": [str(x) for x in p.iterdir()]
    }


def read_file(path):

    try:
        with open(path, "r", encoding="utf-8") as f:
            return {"content": f.read()}
    except Exception as e:
        return {"error": str(e)}


def write_file(path, content):

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return {"success": True}

    except Exception as e:
        return {"error": str(e)}
