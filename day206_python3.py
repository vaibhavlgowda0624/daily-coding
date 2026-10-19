numbers = list(map(
    float,
    input("Enter numbers separated by spaces: ").split()
))

if not numbers:
    print("No numbers provided.")
else:
    numbers.sort()
    middle = len(numbers) // 2

    if len(numbers) % 2 == 1:
        median = numbers[middle]
    else:
        median = (
            numbers[middle - 1] + numbers[middle]
        ) / 2

    print("Sorted numbers:", numbers)
    print("Median:", median)
