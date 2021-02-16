class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.val}"


class BST:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if not self.root:
            self.root = node
        else:
            curr = self.root
            while curr:
                if node.val > curr.val:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = node
                elif node.val < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = node
                else:
                    return

    def preOrder(self, root, arr=[]):
        if not root.left and not root.right:
            return [root.val]

        return [root.val] + self.preOrder(root.left) + self.preOrder(root.right)

    def inOrder(self, root):
        if not root.left and not root.right:
            return [root.val]

        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)

    def postOrder(self, root, arr=[]):
        if not root.left and not root.right:
            return [root.val]

        return self.postOrder(root.left) + self.postOrder(root.right) + [root.val]
