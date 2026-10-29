def max_product(numbers):
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required")

    largest = sorted(numbers)
    return max(
        largest[0] * largest[1],
        largest[-1] * largest[-2]
    )


print(max_product([-10, -3, 2, 8]))
