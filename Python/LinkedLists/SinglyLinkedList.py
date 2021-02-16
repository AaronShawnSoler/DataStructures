class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class SLL:
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
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        return

    # removes node from the tail
    def pop(self):
        if not self.head:
            return

        prev = None
        curr = self.head
        while curr.next:
            prev = curr
            curr = curr.next

        prev.next = None
        self.tail = prev

        return curr

    # adds node to the head
    def unshift(self, val):
        node = Node(val)
        return

    # removes node from the head
    def shift(self):
        return

    # gets node at index
    def get(self):
        return

    # updates value of node at index
    def put(self):
        return

    # inserts node at index
    def insert(self):
        return

    # removes node at index
    def remove(self):
        return

    # reverses the list
    def reverse(self):
        return


sll = SLL()

sll.push(10)
sll.push(20)
sll.show()

sll.pop()
sll.show()
