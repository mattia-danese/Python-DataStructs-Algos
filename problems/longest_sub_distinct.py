"""
Problem statement: Given a string, find the length of the longest substring in 
it with no more than K distinct characters.

"""

def longest_sub(s, k):
    chars = []
    max_length = 0
    count = 0


    for i in range(len(s)):
        if s[i] not in chars:
            chars.append(s[i])

        count += 1

        if len(chars) > k:
            if count - 1 > max_length:
                max_length = count - 1
            
            count = 0
            chars = []

        
        

        

    return len(s) if max_length == 0 else max_length


if __name__ == "__main__":
    s = "aaaaabbbcccdddeeefff"
    k = 6
    print(longest_sub(s,k))


