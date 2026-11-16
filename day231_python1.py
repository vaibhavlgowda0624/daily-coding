from collections import Counter
import re

text = "python java python html java python css html python"

words = re.findall(r"\b\w+\b", text.lower())
frequency = Counter(words)

print(frequency.most_common(3))
