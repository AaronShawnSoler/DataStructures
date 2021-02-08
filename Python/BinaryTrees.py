class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root):
        self.root = root if root else None

    def insert(self, node):
        if not self.root:
            self.root = node
        else:
            while node:
                curr = self.root
                if node.val > curr.val:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = node
                        node = None
                elif node.val < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = node
                        node = None

    def dfsPreOrder(self, root):
        if not root:
            return

        print(root.val)
        self.dfsPreOrder(root.left)
        self.dfsPreOrder(root.right)

    def dfsInOrder(self, root):
        if not root:
            return

        self.dfsPreOrder(root.left)
        print(root.val)
        self.dfsPreOrder(root.right)

    def dfsPostOrder(self, root):
        if not root:
            return

        self.dfsPreOrder(root.left)
        self.dfsPreOrder(root.right)
        print(root.val)
