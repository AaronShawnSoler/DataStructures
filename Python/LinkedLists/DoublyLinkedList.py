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
