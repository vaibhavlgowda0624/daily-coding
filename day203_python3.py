import re

sentence = input("Enter a sentence: ")

cleaned = re.sub(r'\s+', ' ', sentence).strip()

print("Cleaned text:", cleaned)
