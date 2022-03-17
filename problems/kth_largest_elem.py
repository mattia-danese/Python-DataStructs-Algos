"""
    Problem Statement: Design a class to efficiently find the Kth largest element in
    a stream of numbers. The class should have the following two things: ​
        - The constructor of the class should accept an integer array containing 
        initial numbers from the stream and an integer ‘K’.
        - The class should expose a function add(int num) which will store the given
        number and return the Kth largest number.
"""

class Solution:
    def __init__(self, elems, k):
        self.elems = elems
        self.k = k

    def find_k_largest(self):
        arr = self.elems
        arr.sort()
        
        return arr[-self.k]

if __name__ == "__main__":
    s = Solution([1, 384, 293923, 474, 2383, 494 ,99, 4820, 12, 484, 75, 800], 2)
    assert(s.find_k_largest() == 4820)