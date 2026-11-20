def calculate_percentage(obtained, total):
    if total <= 0:
        raise ValueError("Total must be positive")

    if obtained < 0 or obtained > total:
        raise ValueError("Invalid obtained marks")

    return (obtained / total) * 100

print(calculate_percentage(420, 500))
