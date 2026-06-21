import os
from pathlib import Path

ROOT = Path.cwd()

def resolve_path(path):
return ROOT / path

def list_files(path="."):
p = resolve_path(path)
if not p.exists():
return {"error": "path not found"}

```
return {
    "files": sorted(
        [str(x.relative_to(ROOT)) for x in p.rglob("*")]
    )
}
```

def read_file(path):
p = resolve_path(path)

```
if not p.exists():
    return {"error": "file not found"}

with open(p, "r", encoding="utf-8") as f:
    return {"content": f.read()}
```

def write_file(path, content):
p = resolve_path(path)

```
p.parent.mkdir(parents=True, exist_ok=True)

with open(p, "w", encoding="utf-8") as f:
    f.write(content)

return {"success": True}
```

def edit_file(path, content):
return write_file(path, content)
