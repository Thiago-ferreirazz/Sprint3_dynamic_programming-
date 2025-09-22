class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):  # O(1)
        self.items.append(item)

    def dequeue(self):  # O(1)
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def __iter__(self):
        return iter(self.items)
