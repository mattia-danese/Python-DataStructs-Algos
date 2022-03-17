"""
Problem statement: Least Recently Used (LRU) is a common caching strategy. It 
defines the policy to evict elements from the cache to make room for new 
elements when the cache is full, meaning it discards the least recently used 
items first.

"""

class LRUCache():
    def __init__(self):
        self.elems = []
        self.capacity = 10

    def add(self, e):
        if self.__isFull():
            self.remove()
        self.elems.append(e)

    def remove(self):
        self.elems = self.elems[1:]

    def __isFull(self):
        return len(self.elems) == self.capacity

    def print(self):
        print(self.elems)

if __name__ == "__main__":
    c = LRUCache()
    for i in range(10):
        c.add(i)
    c.print()

    c.add(100)
    c.print()

    c.remove()
    c.remove()
    c.print()
