"""
    TIME COMPLEXITY: O(nlogn)

"""

from array import array
from heapq import merge
from turtle import right


def zipper(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_a:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1
    

def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    zipper(left, right, arr)

    