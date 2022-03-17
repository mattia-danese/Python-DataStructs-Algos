"""
STACKS:
    - last in, first out (LIFO)
    - preserves chronological order based on most recent

TIME COMPLEXITY:
    - push/pop: O(1)
    - search by value: O(n)

USE CASES:
    - function stack
        - function calling another function 
    - Ctrl-Z

IMPLEMENTATIONS:
    - list
        - not recommended because of list capacity limitation
    - collections.deque
    - queue.LifoQueue
"""

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        return self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def reverse(self):
        new_deque = deque()
        
        while not self.is_empty():
            new_deque.append(self.pop())

        self.stack = new_deque


def balanced_parens(s):
    stack = Stack()

    for c in s:
        if c == '(':
            stack.push(c)
        if c == ')':
            try:
                stack.pop()
            except:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    s = Stack()
    s.push("1")
    s.push("2")
    s.push("3")
    print(s.pop())
    print(s.pop())
    print(s.pop())
    s.push("1")
    s.push("2")
    s.push("3")
    s.reverse()
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.is_empty())
    print(s.size())

    print(balanced_parens("(((")) #false
    print(balanced_parens("((()))")) #true
    print(balanced_parens("()()()")) #true
    print(balanced_parens("(()()))()(()()((")) #false