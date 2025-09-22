class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):  # O(1)
        self.items.append(item)

    def pop(self):  # O(1)
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def __iter__(self):
        return reversed(self.items)
