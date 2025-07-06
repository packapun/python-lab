# Given a string s, find the length of the longest substring without duplicate characters.


"""
Assumptions:  
Character set -> the english alphabet (a-z), digits, symbols and spaces
Size of the input = 50000
What's the output? Length of the longest substr with unique chars

Example: 
s = "abcabcd"
ans : abc


Simple solve:
1. Find all the substrings (which is the power set)
2. Filter them to only the ones which have unique characters 
3. Return the longest substr out of all

O(2^n)


Improvement: 
Best case -> O(n) lower bound, where n = len(s)
Insight : Only look at each element once at best


Improved Algorithm: 
1. Initialize a hashmap, max and start and store char positions
2. Iterate through each character till the end of the string
3. If char exists in char_map, update the position in the map and move start to the prev_position + 1 and update max_count
4. If char doesn't exist, add it to the map 
5. Return max_count

Runtime = O(n)
Space = O(n)
n = len(s)



char_map = [a:0,b:1,c:2...]
max_length = 0 
start = 0

abcd
[a:3...]


"""


def calculateLongestSubstring(s:str) -> int:
    if not s:
        return 0
    max_count = 0 
    n = len(s)
    char_map = {}
    start = 0 

    for i in range(0,n): 
        char = s[i]
        if char not in char_map:
            char_map[char] = i
        else: 
            index = char_map[char]
            char_map[char] = i
            start = max(start, index+1)
        max_count = max(max_count, i - start + 1)
        print("count={}, start={}, char_map={}".format(max_count,start,char_map))
    return max_count


"""
Example:

abcabcd

[a:3,b:1,c:2...]
i = 3
start = 1 -> b

"""

# Test
s = "aaabaaa"
ret = calculateLongestSubstring(s)
print(f"Max length found in {s} is {ret} ")





