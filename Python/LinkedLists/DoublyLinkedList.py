class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def show(self):
        return

    # adds node to the tail
    def push(self, val):
        node = Node(val)
        if not self.tail:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next

        self.length += 1

        return

    # removes node from the tail
    def pop(self):
        if not self.tail:
            return

        node = self.tail

        self.tail = self.tail.prev
        self.tail.next = None
        if not self.tail:
            self.head = None

        self.length -= 1

        return node

    # adds node to the head
    def unshift(self, val):
        return

    # removes node from the head
    def shift(self):
        return

    # gets node at index
    def get(self, index):
        return

    # updates value of node at index
    def put(self, index, val):
        return

    # inserts node at index
    def insert(self, index, val):
        return

    # removes node at index
    def remove(self, index):
        return

    # reverses the list
    def reverse(self):
        return
