import threading

def task():
    print("Task running in a thread")

thread = threading.Thread(target=task)

thread.start()
thread.join()

print("Main program completed")
