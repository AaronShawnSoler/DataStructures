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

        self.length += 1

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

        self.length -= 1

        return curr

    # adds node to the head
    def unshift(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1

        return

    # removes node from the head
    def shift(self):
        if not self.head:
            return

        node = self.head
        self.head = node.next

        self.length -= 1

        return node

    # gets node at index
    def get(self, index):
        if index < 0 or index > self.length - 1:
            return

        i = 0
        curr = self.head
        while not i == index:
            curr = curr.next
            i += 1

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
            node.next = prev.next
            prev.next = node

        self.length += 1

        return

    # removes node at index
    def remove(self, index):
        if index < 0 or index > self.length - 1:
            return

        node = self.get(index)
        if index == 0:
            node = self.shift()
        elif index == self.length - 1:
            node = self.pop()
        else:
            prev = self.get(index - 1)
            prev.next = prev.next.next

        self.length -= 1

        return node

    # reverses the list
    def reverse(self):
        prev = None
        curr = self.head
        after = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = after
            after = curr.next if curr else None

        self.head, self.tail = self.tail, self.head
        return


sll = SLL()

sll.push(10)
sll.push(20)
sll.show()

sll.insert(1, 30)
sll.show()
sll.insert(1, 40)
sll.show()

sll.reverse()
sll.show()
