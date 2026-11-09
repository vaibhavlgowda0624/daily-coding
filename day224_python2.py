from collections import deque

queue = deque()

queue.append("Student 1")
queue.append("Student 2")
queue.append("Student 3")

print("Queue:", queue)
print("Served:", queue.popleft())
print("Remaining:", queue)
