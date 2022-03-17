"""
Problem statement: Given a string, find if its letters can be rearranged in 
such a way that no two same characters come next to each other.


"""


def longest_sub(s):
    freq = [0 for x in range(26)]

    for i in s:
        freq[ord(i) % 97] += 1

    for f in freq:
        if f > len(s)/2:
            return False

    return True




if __name__ == "__main__":
    s = "aaaaabbbcccdddeeefff"
    assert(longest_sub(s))
    s = "aaaa"
    assert(not longest_sub(s))
    s = "aabb"
    assert(longest_sub(s))

