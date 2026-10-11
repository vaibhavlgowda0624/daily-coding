import time

start = time.perf_counter()

total = sum(range(1_000_001))

end = time.perf_counter()

print("Total:", total)
print("Execution time:", round(end - start, 4), "seconds")
