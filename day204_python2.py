from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import json

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    with urlopen(url, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))

    print("Post ID:", data["id"])

except HTTPError as error:
    print("HTTP error:", error.code)

except URLError as error:
    print("Connection error:", error.reason)

except (TimeoutError, json.JSONDecodeError) as error:
    print("Request or JSON error:", error)
