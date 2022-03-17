"""
Problem statement: Given the root node of a binary tree, swap the 'left' and 
'right' children for each node.

"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


    def get_level(self):
        if self.parent is None:
            return 0

        return self.parent.get_level() + 1

    def get_level_iter(self):
        if self.parent is None:
            return 0

        itr = self.parent
        count = 1
        while itr:
            count += 1
            itr = itr.parent

        return count


    def print(self):
        spaces = '  ' * self.get_level()
        pre = spaces + "|__" if self.parent else "" 
        print(pre, self.val)

        if self.children:
            for c in self.children:
                c.print()

    def print_to_level(self, level):
        spaces = '  ' * self.get_level()
        pre = spaces + "|__" if self.parent else "" 
        print(pre, self.val)

        if self.children and level >= self.get_level()+1:
            for c in self.children:
                c.print_to_level(level)



def mirror(tree):
    if tree.children == []:
        return 
    
    temp = tree.children[0]
    tree.children[0] = tree.children[1]
    tree.children[1] = temp

    mirror(tree.children[0])
    mirror(tree.children[1])

        



def build_tree():
    root = TreeNode("0")

    laptop = TreeNode("1")
    laptop.add_child(TreeNode("3"))
    laptop.add_child(TreeNode("4"))

    cellphone = TreeNode("2")
    cellphone.add_child(TreeNode("5"))
    cellphone.add_child(TreeNode("6"))

    root.add_child(laptop)
    root.add_child(cellphone)

    return root

if __name__ == "__main__":
    tree = build_tree()
    tree.print()

    mirror(tree)
    tree.print()


