numbers = [64, 34, 25, 12, 22, 11]

for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = (
                numbers[j + 1],
                numbers[j]
            )

print("Sorted:", numbers)
