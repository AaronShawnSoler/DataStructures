class Node {
  constructor(val, next) {
    this.val = val ? val : null
    this.next = next ? next : null
  }
}

class SSL {
  constructor() {
    this.length = 0
    this.head = null
    this.tail = null
  }

  /**
   * Prints the linked list
   */
  print() {
    let list = []
    let curr = this.head
    while(curr) {
      list.push(curr.val)
      curr = curr.next
    }

    console.log(list. this.length)
  }

  /**
   * Adds a node to the tail of the linked list
   * @param {*} val - The value for the node
   */
  push(val) {
    // create new node
    let node = new Node(val)

    // if head & tail don't exist create it
    // else add node after tail and set tail to new node
    if(this.head == null) {
      this.head = node
      this.tail = node
    } else {
      this.tail.next = node
      this.tail = node
    }

    // increase length
    this.length++

    return this.length
  }

  /**
   * Removes node from the tail of the linked list
   */
  pop() {
    // if length == 1 set head and tail to null and reduce size
    if(this.length == 1) {
      let node = this.head
      this.head = null
      this.tail = null
      this.length = 0
      return node.val
    }

    // find last node and store prev node
    let prev = null
    let curr = this.tail
    while(curr.next) {
      prev = curr;
      curr = curr.next
    }

    // get last node and remove it
    let node = this.curr
    prev.next = null
    this.tail = prev

    // reduce length
    this.length--

    return node.val
  }

  /**
   * Adds node the head of the linked list
   * @param {*} val 
   */
  unshift(val) {
    // create new node
  }

  /**
   * Removes node from the head of the linked list
   */
  shift() {

  }
}