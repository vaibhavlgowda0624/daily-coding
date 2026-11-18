import re

text = """
Visit https://example.com
Also visit http://python.org
"""

urls = re.findall(r"https?://[^\s]+", text)

for url in urls:
    print(url)
