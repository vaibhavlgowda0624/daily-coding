class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return "Stack is empty"
        return self.items.pop()

    def display(self):
        print(self.items)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.display()
print("Removed:", stack.pop())
