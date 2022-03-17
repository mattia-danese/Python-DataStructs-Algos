"""
ISSUES WITH ARRAYS:
    - going above maximum capacity causes array to be copied and then capacity
    is increase
    - not efficient

BENEFITS OVER ARRAY:
    - no need to pre-allocate space
    - insertion is easier (swaps with indexing)

LINKED LISTS:
    - chain of nodes
    - each node:
        - contains value
        - contains address of next Node

TIME COMPLEXITY: 
    - insert at beginning: O(1)
    - delete at beginning: O(1)
    - insert/delete at end: O(n)
    - lookup by value: O(n)
    - traversal: O(n)

DOUBLE LINKED LIST:
    - same as Linked List but each node also had address of previous node
    - bi-directional
"""

import this


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def print(self):
        return str(self.val) + "," + str(self.next)


class LinkedList:
    def __init__(self):
        self.head = None


    def insert_at_beginning(self, val):
        node = Node(val, self.head)
        self.head = node


    def insert_at_end(self, val):
        if self.head is None:
            self.insert_at_beginning(val)
            return 

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(val, None)


    def insert_values(self, vals):
        for val in vals:
            self.insert_at_end(val)


    def length(self):
        count = 0
        
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count


    def remove_at(self, idx):
        if idx < 0 or idx > self.length():
            raise Exception("Invalid index")
        
        if idx == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                itr.next = itr.next.next
                break 

            itr = itr.next
            count += 1


    def insert_at(self, idx, val):
        if idx < 0 or idx > self.length():
            raise Exception("Invalid index")

        if idx == 0:
            self.insert_at_beginning(val)
            return 

        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                itr.next = Node(val, itr.next.next)
                break 

            itr = itr.next
            count += 1


    def insert_after_value(self, val, new_val):
        if self.head is None:
            raise Exception("Linked List is empty")

        itr = self.head
        while itr:
            if itr.val == val:
                itr.next = Node(new_val, itr.next.next)
                return
            itr = itr.next
        
        raise Exception("Value not in Linked List")


    def remove_by_value(self, val):
        if self.head is None:
            raise Exception("Linked List is empty")

        if self.head.val == val:
            self.head = self.head.next
            return 

        itr = self.head.next
        prev = self.head

        while itr:
            if itr.val == val:
                prev.next = itr.next
                return

            prev = itr
            itr = itr.next
            
        raise Exception("Value not in Linked List")


    def reverse(self):
        if self.head is None:
            raise Exception("Linked List is empty")

        new_list = LinkedList()

        itr = self.head
        while itr:
            new_list.insert_at_beginning(itr.val)
            itr = itr.next

        self.head = new_list.head


    def __reverse_helper(self, node):
        if node.next == None:
            self.head.next = None
            self.head = node
            return node

        prev = self.__reverse_helper(node.next)
        prev.next = node
    
        return node


    def reverse_recursion(self):
        self.__reverse_helper(self.head)


    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        s = ''
        while itr:
            s += str(itr.val)
            if itr.next is not None:
                s += "-->"
            itr = itr.next
            
        print(s)



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(3)
    # ll.insert_at_end(1)
    # ll.insert_at_end(2)
    # ll.insert_at_end(3)
    # ll.print()
    # ll.remove_at(5)
    ll.print()
    # ll.reverse()
    ll.reverse_recursion()
    ll.print()
            