from DoublyLinkedList import DLL

class Queue:
  def __init__(self):
    self.queue = DLL()
    self.size = self.queue.length
  
  def enqueue(self, val):
    self.queue.push(val)
    self.size = self.queue.length
    print(self.size)
  
  def dequeue(self):
    if self.size > 0:
      node = self.queue.shift()
      self.size = self.queue.length
      print(node.val, self.size)
      return node.val

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()