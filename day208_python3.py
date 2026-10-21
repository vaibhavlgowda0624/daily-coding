def binary_search(numbers, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if numbers[middle] == target:
        return middle

    if numbers[middle] < target:
        return binary_search(
            numbers, target, middle + 1, right
        )

    return binary_search(
        numbers, target, left, middle - 1
    )


values = [5, 10, 15, 20, 25, 30, 35]
target = int(input("Enter target: "))

index = binary_search(values, target, 0, len(values) - 1)

print("Index:", index if index != -1 else "Not found")
