"""
Problem statement: You are given an array (list) of interval pairs as input 
where each interval has a start and end timestamp. The input array is sorted by 
starting timestamps. You are required to merge overlapping intervals and return
output array (list).

"""


def merge(arr):
    i = 1

    while i < len(arr):
        this_start = arr[i][0]
        this_end = arr[i][1]

        prev_start = arr[i-1][0]
        prev_end = arr[i-1][1]

        if this_start < prev_end:
            new_start = prev_start
            new_end = max(this_end, prev_end)
            del arr[i], arr[i-1]
            arr.insert(i-1, (new_start, new_end))
        else:
            i += 1

    return arr

if __name__ == "__main__":
    arr = [
       (1,4),
       (2,7), 
       (11,20),
       (12,18),
       (19, 21), 
       (22, 30)
    ]

    arr2 = [
        (1, 4),
        (1, 4),
        (1, 4),      
    ]

    arr3 = [
        (1, 4),
        (5,6),
        (9,10)
    ]

    arr = merge(arr)
    arr2 = merge(arr2)
    arr3 = merge(arr3)
    
    print(arr)
    print(arr2)
    print(arr3)

        



