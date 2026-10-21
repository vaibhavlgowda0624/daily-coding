numbers = [1, 3, 4, 6, 8, 10, 13]
target = int(input("Enter target sum: "))

left = 0
right = len(numbers) - 1
found = False

while left < right:
    total = numbers[left] + numbers[right]

    if total == target:
        print("Pair:", numbers[left], numbers[right])
        found = True
        break
    elif total < target:
        left += 1
    else:
        right -= 1

if not found:
    print("No pair found.")
