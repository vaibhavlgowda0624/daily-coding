from collections import Counter

numbers = [4, 7, 4, 2, 7, 4, 9, 7, 4]

frequency = Counter(numbers)

most_common = frequency.most_common(1)

print("Most frequent:", most_common[0][0])
print("Frequency:", most_common[0][1])
