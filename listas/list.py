from .node import Node

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def setSize(self, size):
        self.size = size

    def first(self):
        if self.isEmpty():
            return None
        return self.head.get_data()

    def last(self):
        if self.isEmpty():
            return None
        return self.tail.get_data()

    def addFirst(self, data):
        newest = Node(data)
        if self.isEmpty():
            self.tail = newest
        newest.set_next(self.head)
        self.head = newest
        self.size += 1

    def addLast(self, data):
        newest = Node(data)
        if self.isEmpty():
            self.head = newest
        else:
            self.tail.set_next(newest)
        self.tail = newest
        self.size += 1
