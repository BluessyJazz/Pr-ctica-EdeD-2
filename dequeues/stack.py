'''import sys

sys.path.append("..")'''
from practica_eded_2.listas.list import List

'''.listas.list import List'''

class Stack:
    def __init__(self):
        self.items = List()

    def is_empty(self):
        return self.items.is_empty()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            item = self.items.head.get_data()
            self.items.remove(item)
            return item

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.items.head.get_data()
