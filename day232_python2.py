import threading
import time

def worker(number):
    print(f"Worker {number} started")
    time.sleep(1)
    print(f"Worker {number} completed")

threads = []

for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All workers completed")
