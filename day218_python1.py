numbers = [2, 4, 6, 1, 3, 5, 7, 2]

longest = current = 1
start = best_start = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        current += 1
    else:
        current = 1
        start = i

    if current > longest:
        longest = current
        best_start = start

print(numbers[best_start:best_start + longest])
