from pathlib import Path

def search(query, folder="."):
    for path in Path(folder).glob("*.txt"):
        text = path.read_text(encoding="utf-8")
        if query.lower() in text.lower():
            print(path.name, text[:200])

if __name__ == "__main__":
    search(input("Search query: "))