from DoublyLinkedList import DLL

class Stack:
  def __init__(self):
    self.stack = DLL()
    self.size = self.stack.length

  def push(self,val):
    self.stack.push(val)
    self.size = self.stack.length

  def pop(self):
    if self.size > 0:
      node = self.stack.pop()
      self.size = self.stack.length
      return node.val