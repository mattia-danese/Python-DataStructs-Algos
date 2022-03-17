"""
TREE:
    - for heirarchy data
    - recursive data structure (child of tree node is a tree itself)




"""

from tkinter.tix import Tree
from webbrowser import get


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

            


def build_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))
    
    cellphone = TreeNode("Cellphone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivio"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root



if __name__ == "__main__":
    root = build_tree()
    root.print_to_level(3)
