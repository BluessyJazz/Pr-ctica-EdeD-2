# queue.py
from listas.list import List  # Importa la clase List para usarla en Queue

class Queue:
    def __init__(self):
        self.list = List()

    def isEmpty(self):
        return self.list.isEmpty()
    
    def size(self):
        return self.list.size()

    def enqueue(self, item):
        self.list.addLast(item)

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            return self.list.removeFirst()
        

    def first(self):
        if self.isEmpty():
            return None
        else:
            return self.list.first()
