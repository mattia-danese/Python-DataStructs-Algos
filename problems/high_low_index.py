"""
Problem statement: Given a sorted array of integers, return the low and high 
index of the given key. Return -1 if not found. The array length can be in 
the millions with many duplicates.
"""

from operator import truediv
from random import randint

def find_idxs(arr, k):
    if k not in arr:
        return -1

    i = 0
    j = len(arr) - 1

    found_low = False
    found_high = False

    low = -1
    high = -1

    while i < len(arr) and j >= 0:
        if arr[i] == k and not found_low:
            low = i
            found_low = True

        if arr[j] == k and not found_high:
            high = j
            found_high = True

        i += 1
        j -= 1

    return (low, high)

if __name__ == "__main__":
    arr = [randint(1,20) for _ in range(100)]
    print(arr)
    print(" ")
    print(arr[::-1])
    print(" ")

    print(find_idxs(arr, 15))

