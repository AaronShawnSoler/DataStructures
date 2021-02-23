class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"{'None <- ' if not self.prev else ''}{self.val} -> {'<-' if self.next and self.next.prev else ''} {self.next}"


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
            node.prev = self.tail
            self.tail.next = node
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

        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = self.head.prev

        self.length += 1

        return

    # removes node from the head
    def shift(self):
        if not self.head:
            return

        node = self.head

        self.head = self.head.next
        self.head.prev = None
        if not self.head:
            self.tail = None

        self.length -= 1

        return node

    # gets node at index
    def get(self, index):
        if index < 0 or index > self.length - 1:
            return

        if index <= (self.length - 1) // 2:
            i = 0
            curr = self.head
            while not i == index:
                curr = curr.next
                i += 1
        else:
            i = self.length - 1
            curr = self.tail
            while not i == index:
                curr = curr.prev
                i -= 1

        print(curr.val)
        return curr

    # updates value of node at index
    def put(self, index, val):
        if index < 0 or index > self.length - 1:
            return

        node = self.get(index)
        node.val = val

        return

    # inserts node at index
    def insert(self, index, val):
        if index < 0 or index > self.length - 1:
            return

        if index == 0:
            self.unshift(val)
        else:
            node = Node(val)
            prev = self.get(index - 1)
            node.prev = prev
            node.next = prev.next
            if prev.next:
                prev.next.prev = node
            prev.next = node
            self.length += 1

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
dll.unshift(1)
dll.unshift(2)
dll.unshift(3)

dll.show()

dll.pop()
dll.show()

dll.shift()
dll.show()

dll.get(0)
dll.get(1)
dll.get(2)
dll.get(3)

dll.insert(2, 54)
dll.insert(0, 45)
dll.insert(5, 100)
dll.show()
