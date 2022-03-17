def bs_iterative(arr, k):
    left_idx = mid_idx = 0
    right_idx = len(arr)-1


    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        mid_num = arr[mid_idx]

        if mid_num == k:
            return mid_idx

        if mid_num < k:
            left_idx = mid_idx + 1

        if mid_num > k:
            right_idx = mid_idx - 1

    return -1


def bs_recursive(arr, k, left_idx, right_idx):
    if right_idx < left_idx:
        return -1

    mid_idx = (left_idx + right_idx) // 2
    mid_num = arr[mid_idx]

    if mid_num == k:
            return mid_idx

    if mid_num < k:
        left_idx = mid_idx + 1

    if mid_num > k:
        right_idx = mid_idx - 1

    bs_recursive(arr, k, left_idx, right_idx)