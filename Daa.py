class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.max_size

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            print("Stack is full. Cannot push element.")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop element.")
            return None

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. No top element.")
            return None

# Create a stack with a maximum size of 5
stack = Stack(max_size=5)

# Push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Check if the stack is empty
print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False

# Check if the stack is full
print("Is stack full?", stack.is_full())    # Output: Is stack full? False

# Return the top element
print("Top element:", stack.top())          # Output: Top element: 30

# Pop elements from the stack
print("Popped element:", stack.pop())       # Output: Popped element: 30
print("Popped element:", stack.pop())       # Output: Popped element: 20

# Pop from an empty stack
print("Popped element:", stack.pop())       # Output: Stack is empty. Cannot pop element. Popped element: None
