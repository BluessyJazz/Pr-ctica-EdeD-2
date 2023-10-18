# queue.py
from listas.list import List  # Importa la clase List para usarla en Queue

class Queue:
    def __init__(self):
        self.list = List()

    def is_empty(self):
        return self.list.is_empty()

    def enqueue(self, item):
        self.list.add(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        else:
            current = self.list.head
            previous = None
            while current.get_next() is not None:
                previous = current
                current = current.get_next()
            if previous is None:
                self.list.head = None
            else:
                previous.set_next(None)
            return current.get_data()

    def first(self):
        if self.is_empty():
            return None
        else:
            current = self.list.head
            while current.get_next() is not None:
                current = current.get_next()
            return current.get_data()
