from listas.list import List

class Queue:
    def __init__(self):
        self.items = List()

    def is_empty(self):
        return self.items.is_empty()

'''    def enqueue(self, item):
        self.items.add(item)
'''

    # Modificación del método enqueue en la implementación de Queue
    def enqueue(self, item):
        current = self.items.head
        if current is None:
            self.items.add(item)
        else:
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(Node(item))

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            item = self.items.head.get_data()
            self.items.remove(item)
            return item

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            return self.items.head.get_data()
