from .double_node import DoubleNode

class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.get_data()
            self.current = self.current.get_next()
            return data

    def isEmpty(self):
        return self.size == 0

    def first(self):
        if self.isEmpty():
            return None
        return self.head.get_data()

    def last(self):
        if self.isEmpty():
            return None
        return self.tail.get_data()

    def addFirst(self, data):
        new_node = DoubleNode(data)
        if self.isEmpty():
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
        self.head = new_node
        self.size += 1

    def addLast(self, data):
        new_node = DoubleNode(data)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.set_prev(self.tail)
            self.tail.set_next(new_node)
        self.tail = new_node
        self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            return None
        data = self.head.get_data()
        self.head = self.head.get_next()
        if self.head is None:
            self.tail = None
        else:
            self.head.set_prev(None)
        self.size -= 1
        return data

    def removeLast(self):
        if self.isEmpty():
            return None
        data = self.tail.get_data()
        self.tail = self.tail.get_prev()
        if self.tail is None:
            self.head = None
        else:
            self.tail.set_next(None)
        self.size -= 1
        return data

    def remove(self, node):
        prev = node.get_prev()
        next = node.get_next()
        if prev is not None:
            prev.set_next(next)
        else:
            self.head = next
        if next is not None:
            next.set_prev(prev)
        else:
            self.tail = prev
        self.size -= 1
        return node.get_data()

    def addBefore(self, node, data):
        if node is None:
            return self.addFirst(data)
        new_node = DoubleNode(data)
        new_node.set_next(node)
        prev = node.get_prev()
        new_node.set_prev(prev)
        node.set_prev(new_node)
        if prev is not None:
            prev.set_next(new_node)
        else:
            self.head = new_node
        self.size += 1

    def addAfter(self, node, data):
        if node is None:
            return self.addLast(data)
        new_node = DoubleNode(data)
        new_node.set_prev(node)
        next = node.get_next()
        new_node.set_next(next)
        node.set_next(new_node)
        if next is not None:
            next.set_prev(new_node)
        else:
            self.tail = new_node
        self.size += 1

    def search(self, target):
        current = self.head
        while current is not None:
            if current.get_data() == target:
                return True
            current = current.get_next()
        return False
    

    def addOrder(self, data):
        new_node = DoubleNode(data)
        if self.isEmpty() or data < self.head.get_data():
            self.addFirst(data)
        elif data > self.tail.get_data():
            self.addLast(data)
        else:
            current = self.head
            while current.get_data() < data:
                current = current.get_next()
            prev_node = current.get_prev()
            self.addBefore(current, data)

