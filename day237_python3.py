from collections import Counter

def first_unique(text):
    counts = Counter(text)

    for char in text:
        if counts[char] == 1:
            return char

    return None

print(first_unique("programming"))
