questions = [
    ("Which keyword defines a function in Python?", "def"),
    ("Which data type stores key-value pairs?", "dict"),
    ("Which symbol starts a comment?", "#")
]

score = 0

for question, answer in questions:
    print("\n" + question)
    user_answer = input("Answer: ").strip().lower()

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Correct answer:", answer)

print(f"\nFinal score: {score}/{len(questions)}")
