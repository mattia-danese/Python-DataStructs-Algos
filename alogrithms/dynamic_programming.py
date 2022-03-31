
"""
TRIVIAL SOLUTION: O(2^n) time
Many redundant function calls, recomputing fib(0), fib(1), etc. many
"""
def fib(n):
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)

"""
DYNAMIC PROGRAMMING SOLUTION: O(n)
'memory' makes it so each fib number needs to be calculated only once, all other
times a lookup is solely needed
"""
def fib_memoization(n, memory={}):
    if n < 2:
        return n

    if n in memory:
        return memory[n]

    memory[n] = fib_memoization(n-1, memory) + fib_memoization(n-2, memory)
    return memory[n]


"""
TRIVIAL SOLUTION: O(n^2) time
Calculates every possible subarray and stores the absolute minimum
"""
def min_subarray_sum(arr):
    if len(arr) == 0:
        return 0

    min_sum = None

    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            sub = arr[i:j]
            min_sum = min(min_sum, sub)

    return min_sum

"""
DYNAMIC PROGRAMMING SOLUTION: O(n) time
Subarray must be continuous, so problem can be broken down into "if i were to use
the current elem, should i use the previous elem(s) or would i make a lower sum
by using only the current elem".

OPTIMIZE: O(n) --> O(1) space
Can be optimized by making 'min_sum_with_prev_elem' store just the previous
curr_min, does not have to be an array
"""


def min_subarray_sum_dp(arr):
    if len(arr) == 0:
        return 0

    min_sum_with_prev_elem = [arr[0]]
    min_sum = arr[0]

    for i in range(1, len(arr)):
        num = arr[i]
        curr_min = min(num, num + min_sum_with_prev_elem[i-1])
        min_sum_with_prev_elem.append(curr_min)
        min_sum = min(min_sum, curr_min)

    return min_sum