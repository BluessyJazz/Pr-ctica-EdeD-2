from listas.list import List


class Stack:
    def __init__(self):
        self.list = List()

    def isEmpty(self):
        return self.list.isEmpty()
    
    def size(self):
        return self.list.size()

    def push(self, item):
        self.list.addFirst(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.list.removeFirst()

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.list.first()
