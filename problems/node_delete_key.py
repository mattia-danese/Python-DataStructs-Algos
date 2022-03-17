"""
    Problem statement: You are given the head of a linked list and a key. 
    You have to delete the node that contains this given key.

"""

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

class Solution:
    def __init__(self, ll, k):
        self.ll = ll
        self.k = k

    def delete_key(self):
        if self.ll.head.val == self.k:
            self.ll.head = self.ll.head.next
            return 

        itr = self.ll.head.next
        prev = self.ll.head

        while itr:
            if itr.val == self.k:
                prev.next = itr.next
                return 
            
            itr = itr.next

    def print(self):
        self.ll.print()

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(3)

    s = Solution(ll, 2)
    s.delete_key()
    s.print()

