"""
TIME COMPLEXITY:
    - lookup by index: O(1)
    - lookup by value: O(n)
    - traversal: O(n)
    - insertion: O(n), will shift right
    - deletion: O(n), will shift left


STATIC ARRAY: fixed length (determined in declaration)
    - fixed length is stored memory

DYNAMIC ARRAY: no fixed length (can keep adding items)
    - on declaration, has initial size in memory
    - when initial size is not enough, array is copied to new memory and the 
    size will increase by multiple of 3
        - 'copied' array not necessarily in same place in memory because
        other variables/stuff might be stored in surrounding memory addresses
    - python List
"""

arr = [1, 2, 3]
arr = [x for x in range(10)]