"""
BINARY TREES:
    - every node has at most 2 child nodes
    - no duplicate values (unique)

BINARY SEARCH TREES:
    - binary tree but with the added condition that all descendents to the left
    of node are less in value and all descendents to the right of node are greater
    in value

SEARCH COMPLEXITY:
    - every iteration in search, we reduce search space by 1/2
    - O(log n)

INSERTION COMPLEXITY:
    - O(log n)

SEARCHING METHODS:
    - Bread First Search
        - current nodes first
    - Depth First Search
        - children nodes first
    - Traversals (relative to root node)
        - In Order
            - working from all the way left to all the way right
            - root node is visited in order
        - Pre Order
            - left subtree, then right subtree, all the way down
            - root is visited first
        - Post Order
            - left subtree, then right subtree, all the way up
            - root is visited last

DELETION:
    - no child
        - just remove node from being child of parent
    - one child
        - just remove it and pass its child as the new child of parent
    - two children
        - must ensure BST properites are not compromised
        - replace node with minimum value from right subtree
            - garantees all nodes from right subtree are greater than node
        - replace node with maximum value from left subtree
            - garantees all nodes from left subtree are less than node

"""


class BinarySearchTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add_child(self, val):
        if self.val == val: # no duplicates
            return 

        if self.val > val: # adding to left subtree
            if self.left: # checking if at leaf node
                self.left.add_child(val)
            else:
                self.left = BinarySearchTreeNode(val)
        else: # adding to right subtree
            if self.right: #checking if at leaf node
                self.right.add_child(val)
            else:
                self.right = BinarySearchTreeNode(val)

    def in_order_trav(self):
        elems = []
        
        if self.left:
            elems += self.left.in_order_trav()

        elems += [self.val]

        if self.right:
            elems += self.right.in_order_trav()

        return elems

    def pre_order_trav(self):
        elems = [self.val]
        
        if self.left:
            elems += self.left.pre_order_trav()

        if self.right:
            elems += self.right.pre_order_trav()

        return elems

    def post_order_trav(self):    
        elems = []
        
        if self.left:
            elems += self.left.post_order_trav()

        if self.right:
            elems += self.right.post_order_trav()

        return elems + [self.val]

    def search(self, val):
        if self.val == val:
            return True

        if self.val > val:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()

        return self.val

    def find_max(self):
        if self.right:
            return self.right.find_max()
        
        return self.val

    def calculate_sum(self):
        return sum(self.in_order_trav())

    def delete(self, val):
        if self.val > val:
            if self.left:
                self.left = self.left.delete(val)
        elif self.val < val:
            if self.right:
                self.right = self.right.delete(val)
        else: 
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            # min_val = self.right.find_min()
            # self.val = min_val
            # self.right = self.right.delete(min_val)

            max_val  = self.left.find_max()
            self.val = max_val
            self.left = self.left.delete(max_val)

        return self


def build_tree(elems):
    root = BinarySearchTreeNode(elems[0])
    for i in range(1,len(elems)):
        root.add_child(elems[i])

    return root

if __name__ == "__main__":
    root = build_tree([17, 4, 1, 20, 9, 23, 18, 34, 17])
    print(root.in_order_trav())
    # print(root.pre_order_trav())
    # print(root.post_order_trav())
    # print(root.search(100))
    # print(root.find_min())
    # print(root.find_max())
    # print(root.calculate_sum())
    root.delete(20)
    print(root.in_order_trav())

