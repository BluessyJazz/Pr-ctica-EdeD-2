from .double_node import DoubleNode

class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = DoubleNode(item)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            temp.set_prev(self.tail)
            self.tail.set_next(temp)
            self.tail = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        if found:
            if current == self.head:
                self.head = current.get_next()
                if self.head is not None:
                    self.head.set_prev(None)
            elif current == self.tail:
                self.tail = current.get_prev()
                if self.tail is not None:
                    self.tail.set_next(None)
            else:
                prev_node = current.get_prev()
                next_node = current.get_next()
                prev_node.set_next(next_node)
                next_node.set_prev(prev_node)
