from DoublyLinkedList import DLL

class Stack:
  def __init__(self):
    self.stack = DLL()
    self.size = self.stack.length

  def push(self,val):
    self.stack.push(val)
    self.size = self.stack.length
    print(self.size)

  def pop(self):
    if self.size > 0:
      node = self.stack.pop()
      self.size = self.stack.length
      print(node.val, self.size)
      return node.val

s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.pop()
s.pop()
s.pop()
s.pop()