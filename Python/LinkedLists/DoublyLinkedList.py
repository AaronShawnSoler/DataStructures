class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"{self.val} -> {'<-' if self.next and self.next.prev else ''} {self.next}"


class DLL:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def show(self):
        print(self.head)

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
        node = Node(val)
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


dll = DLL()

dll.push(10)
dll.push(20)
dll.push(30)

dll.show()
