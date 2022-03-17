"""
    Problem Statement: Given a sorted number array and two integers 'K' and 'X', 
    find 'K' closest numbers to 'X; in the array. Return the numbers in the sorted 
    order. 'X' is not necessarily present in the array.

"""

class Solution:
    def __init__(self, elems, k, x):
        self.elems = elems
        self.x = x
        self.k = k

    def helper(self, x, included=True):
        nums = []
        
        idx = self.elems.index(x)
        i = idx - 1
        j = idx + 1
        i_done = j_done = False

        if not included:
            nums.append(x)

        while len(nums) < self.k:
            if i >= 0:
                nums.append(self.elems[i])
                i -= 1
            else:
                i_done = True

            if j < len(self.elems):
                nums.append(self.elems[j])
                j += 1
            else:
                j_done = True

            if i_done and j_done:
                break

        return nums[:k]
    
    def find_k_closest(self):
        if self.x in self.elems:
            return self.helper(self.x)
        else:
            min_diff = abs(self.x - self.elems[0])
            close = self.elems[0]

            for e in self.elems:
                if abs(self.x - e) < min_diff:
                    min_diff = abs(self.x - e) 
                    close = e
        
            return self.helper(close, False)

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9]
    x = 10
    k = 3
    s = Solution(nums,k,x)
    assert(set(s.find_k_closest()) == set([7,8,9]))


    
        

                
