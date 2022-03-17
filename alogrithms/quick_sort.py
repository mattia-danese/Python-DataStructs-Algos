"""
    TIME COMPLEXITY: O(nlogn), average case
                     O(n^2), worse case (if already sorted)
"""
def swap(a,b,arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def partition(arr, start, end):
    pivot_idx = start
    pivot = arr[pivot_idx]

    while start < end:
        print(start, end)
        while start < len(arr) and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

    if start < end:
        swap(start, end, arr)

    swap(pivot_idx, end, arr)

    return end


def quick_sort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        
        quick_sort(arr, start, p - 1) #left partition
        quick_sort(arr, p + 1, end) # right partition

if __name__ == "__main__":
    arr = [9,1,7,13,6,5]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)