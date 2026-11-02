questions = [
    ("What is 2 ** 3?", "8"),
    ("Which keyword defines a function?", "def"),
    ("What data type stores True or False?", "bool")
]

score = 0

for question, answer in questions:
    user_answer = input(question + " ").strip()

    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Answer:", answer)

print(f"Final score: {score}/{len(questions)}")
