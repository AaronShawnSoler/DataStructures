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
   * @param {*} val - The value for the new node
   */
  push(val) {
    // create new node
    let newNode = new Node(val)

    // if length == 0 create first node
    // else add node after tail and set tail to new node
    if(this.length == 0) {
      this.head = newNode
      this.tail = newNode
    } else {
      this.tail.next = newNode
      this.tail = newNode
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
   * @param {*} val - The value for the new node 
   */
  unshift(val) {
    // create new node
    let newNode = new Node(val)

    // if length == 0 create first node
    // else add node after tail and set tail to new node
    if(this.length == 0) {
      this.head = newNode
      this.tail = newNode
    } else {
      newNode.next = this.head
      this.head = newNode
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
   * @param {number} index - Index of node
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
   * @param {number} index - Index of node you want to set
   * @param {*} val - Value you want to set for specified index
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
   * @param {number} index - Index you want to insert node at
   * @param {*} val - Value of new node at specifed index
   */
  insert(index, val) {
    // There's no pre-exsisting index
    if(this.length == 0) return

    // if index is invalid return undefined
    if(index < 0 || index > this.length - 1) return

    // create new node
    let newNode = new Node(val)

    // if index is at head insert at head using unshift
    // if index is at tail insert at tail using push
    // else insert node at index
    if(index == 0) {
      this.unshift(val)
    } else if (index == this.length - 1) {
      this.push(val)
    } else {
      // get node at previous index
      let node = this.get(index - 1)

      // insert node
      newNode.next = node.next
      node.next = newNode

      // increase length
      this.length++
    }

    return this.length
  }

  /**
   * Removes node at specifed index
   * @param {number} index 
   */
  remove(index) {
    // There's nothing to remove
    if(this.length == 0) return

    // if index is invalid return undefined
    if(index < 0 || index > this.length - 1) return

    // if index is at head shift node
    // if index is at tail pop node
    // else remove node at index
    if(index == 0) {
      this.shift()
    } else if(index == this.length - 1) {
      this.pop()
    } else {
      // get node at previous index
      let node = this.get(index - 1)

      // remove node
      node.next = node.next.next

      // reduce length
      this.length--
    }

    return this.length
  }

  /**
   * Reverses linked list
   */
  reverse() {
    let prev = null
    let curr = this.head
    let next = curr.next
    while(curr) {
      curr.next = prev
      prev = curr
      curr = next
      next = curr ? curr.next : null
    }

    [this.head, this.tail] = [this.tail, this.head]

    this.print()
  }
}

let sll = new SLL()

sll.push(1)
sll.push(2)
sll.push(3)