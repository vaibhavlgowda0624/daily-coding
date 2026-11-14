def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"

    return sum(numbers) / len(numbers)


print(calculate_average([10, 20, 30]))
