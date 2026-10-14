import json
from urllib.request import urlopen

url = "https://jsonplaceholder.typicode.com/posts/1"

with urlopen(url, timeout=10) as response:
    data = json.loads(response.read().decode("utf-8"))

print("Title:", data["title"])
print("Content:", data["body"])
