"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
 
        #Value is less than current node
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        
        #Value is greater than OR EQUAL TO current node
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #Base case
        if target == self.value:
            return True
        
        #left traversal
        elif target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)

        #right traversal
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)

        #was not found
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left is not None:
            self.left.for_each(fn)

        if self.right is not None:
            self.right.for_each(fn)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #check if it has children
        if node.left is not None and node.right is not None:
            print(node.value)
            return
        
        if node.left is not None:
            self.in_order_print(node.left)

        if node.right is not None:
            self.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
#############################################################
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_end(value)

    def dequeue(self):
        if(self.size == 0):
            return None
        self.size -= 1
        return self.storage.remove_from_head()

class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
    def __init__(self):
        # first node in the list 
        self.head = None
        # last node in the linked list 
        self.tail = None

    # O(1)
    def add_to_head(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node 
        else:
            new_node.set_next(self.head)
            self.head = new_node

    # we have access to the end of the list, so we can directly add new nodes to it 
    # O(1)
    def add_to_end(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node 
        new_node = Node(value)
        # what if the list is empty? 
        if not self.head and not self.tail:
            # set both head and tail to the new node 
            self.head = new_node
            self.tail = new_node
        # what if the list isn't empty?
        else:
            # set the current tail's next to the new node 
            self.tail.set_next(new_node)
            # set self.tail to the new node 
            self.tail = new_node

    # we already have access to the head of the linked list, so we can directly remove from it 
    # O(1)
    def remove_from_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head 
            value = self.head.get_value()
            # remove the value at the head 
            # update self.head 
            self.head = self.head.get_next()
            return value

    # iterate over our linked list and print out each value in it 
    def print_ll_elements(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.get_next()