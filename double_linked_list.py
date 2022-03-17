class DoubleNode:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def print(self):
        return str(self.prev) + "," + str(self.val) + "," + str(self.next)

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def insert_at_beginning(self, val):
        node = DoubleNode(val, None, self.head)

        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            return

        self.head.prev = node
        self.head = node

    def insert_at_end(self, val):
        node = DoubleNode(val, self.tail, None)

        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node


    def insert_values(self, vals):
        for v in vals:
            self.insert_at_end(v)
    

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
            self.head.next.prev = None
            self.head = self.head.next
            return

        if idx == self.length() - 1:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return 

        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                itr.next.next.prev = itr
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

        if idx == self.length() - 1:
            self.insert_at_end(val)
            return

        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                node = DoubleNode(val, itr, itr.next.next)
                itr.next = node
                itr.next.next.prev = node
                break  

            itr = itr.next
            count += 1


    def insert_after_value(self, val, new_val):
        if self.head is None:
            raise Exception("Linked List is empty")

        itr = self.head
        while itr:
            if itr.val == val:
                node = DoubleNode(new_val, itr, itr.next.next)
                itr.next = node
                itr.next.next.prev = node
                return
            itr = itr.next

        raise Exception("Value not in Linked List")


    def remove_by_value(self, val):
        if self.head is None:
            raise Exception("Linked List is empty")

        if self.head.val == val:
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head.next
        while itr:
            if itr.val == val:
                itr.prev.next = itr.next
                itr.next.prev = itr.prev
                return

            itr = itr.next
            
        raise Exception("Value not in Linked List")


    def reverse(self):
        itr = self.head
        self.head = self.tail
        self.tail = itr
        
        while itr:
            temp = itr.next
            itr.next = itr.prev
            itr.prev = temp

            itr = itr.prev


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

    def get_head(self):
        return self.head.val

    def get_tail(self):
        return self.tail.val

if __name__ == '__main__':
    ll = DoubleLinkedList()
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(3)

    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)

    ll.insert_values([9,9,10])
    ll.print()
    ll.remove_at(0)
    ll.print()
    ll.remove_at(4)
    ll.print()
    ll.remove_at(6)
    ll.print()
    ll.insert_at(3, 11)
    ll.insert_after_value(11, 100)
    ll.print()
    ll.remove_by_value(1)
    ll.print()
    ll.remove_by_value(100)
    ll.print()
    ll.reverse()

    ll.print()
    print("length:", ll.length())
    print("head:", ll.get_head())
    print("tail:", ll.get_tail())