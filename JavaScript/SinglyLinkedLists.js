class Node {
  constructor(val, next) {
    this.val = val ? val : null
    this.next = next ? next : null
  }
}

class SLL {
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

    console.log(list, this.length)
  }

  /**
   * Adds a node to the tail of the linked list
   * @param {*} val - The value for the node
   */
  push(val) {
    // create new node
    let node = new Node(val)

    // if length == 0 create first node
    // else add node after tail and set tail to new node
    if(this.length == 0) {
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
    // if length == 0 return undefined
    if(this.length == 0) return

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
    let node = new Node(val)

    // if length == 0 create first node
    // else add node after tail and set tail to new node
    if(this.length == 0) {
      this.head = node
      this.tail = node
    } else {
      node.next = this.head
      this.head = node
    }

    // increase length
    this.length++

    return this.length
  }

  /**
   * Removes node from the head of the linked list
   */
  shift() {
    // if length == 0 return undefined
    if(this.length == 0) return

    // get node and remove it from head
    let node = this.head
    this.head = node.next

    // reduce length
    this.length--

    return node.val
  }

  /**
   * Gets a node at specified index
   * @param {*} index - index of node
   */
  get(index) {
    // if index is invalid return undefined
    if(index < 0 || index > this.length - 1) return

    // initialize index we're currently on
    let idx = 0
    
    // find node at index
    let curr = this.head
    while(curr) {
      if(idx == index) return curr
      curr = curr.next
      idx++
    }
  }

  /**
   * Sets val of node at specifed index
   * @param {*} index - index of node you want to set
   * @param {*} val - val you want to set for specified index
   */
  set(index, val) {
    // get node at index
    let node = this.get(index)

    // if node is undefined return false
    if(!node) return false

    // set value of node
    node.val = val

    return true
  }

  /**
   * Inserts a new node at specified index
   * @param {*} index - index you want to insert node at
   * @param {*} val - value of new node at specifed index
   */
  insert(index, val) {

  }

  /**
   * Removes node at specifed index
   * @param {*} index 
   */
  remove(index) {

  }

  /**
   * Reverses linked list
   */
  reverse() {

  }
}