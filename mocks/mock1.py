from typing import List

def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()

'''
Given two sorted arrays of integers, your task is to write a function 'minimumN' to return the 'n' smallest integers in sorted order.

Example input:
var arr1 = new int[]{1, 2, 4, 12};
var arr2 = new int[]{3, 6, 7, 19};
var n = 5;
var res = minimumN(arr1, arr2, n);

Example output:
[1, 2, 3, 4, 6]
'''

"""

[1,2,4,12]
[3,6,7,19]

i = 0 -> 2
i += 1

j = 0 -> 3
j += 1

output = [1,]
O(n) -> time and space 

case n > number of elements, return best possible ouput
a1: [1]
a2: [2]
n = 5

a1: [1] 
a2: [2,3,4]
n = 10


a1 = []
a2 = []
ret = []

[1,2,3]
[4,5,6]
[6,7,8]

0 : 1
1 : 0
2 : 0

m lists of max size k
n smallest 


[elem, list, index]

loop thru the heap n times and each iteration you pluck the head of the heap and add the next element that you plucked


Assumptions -> clarifying questions (3) -> edge cases -> brute force approach -> approach -> implementation -> testing (dry run)
"""


# def minimumN(arr1:List[int],arr2:List[int],n:int) -> List[int]:
#     ## Base case 
#     if not arr1 and not arr2:
#         return []

#     i = 0
#     j = 0
#     output = []

#     for _ in range(0,n):
#         if i < len(arr1):
#             if arr1[i] < arr2[j]:
#                 output.append(arr1[i])
#                 i += 1
#         elif j < len(arr2):
#             if arr1[j] <= arr2[i]:
#                 output.append(arr2[j])
#                 j += 1
#     return output 

# 
# TC: O(n), SC:O(n)
def minimumN(arr1:List[int],arr2:List[int],n:int) -> List[int]:
    ## Base case 
    if not arr1 and not arr2:
        return []

    i = 0 # 1
    j = 0
    p = len(arr1)
    q = len(arr2)
    k = 0 
    output = []
    
    while k < n: # 0 < 5
        if i >= p or j >= q: # false
            break

        if arr1[i] < arr2[j]: # true
            output.append(arr1[i])
            i += 1
        else:
            output.append(arr2[j])
            j += 1
        k += 1
    
    ## Handle the remaining elements 
    while i < p and k < n:
        output.append(arr1[i])
        i += 1
        k += 1
    
    while j < q and k < n:
        output.append(arr2[j])
        j += 1
        k += 1

    return output 


def test_minimumN():
    arr1 = [1, 2, 4, 12]
    arr2 = [3, 6, 7, 19]
    n = 5 
    expected_output = [1, 2, 3, 4, 6]
    assert minimumN(arr1,arr2,n) == expected_output

def test_minimumN_variable_length():
    arr1 = [1, 2, 4, 12]
    arr2 = [3,4]
    n = 5
    expected_output = [1,2,3,4,4]
    assert minimumN(arr1,arr2,n) == expected_output

# r2 > r1 
def test_minimumN_r2_greater():
    arr1 = [1, 2]
    arr2 = [3,5,6,7,8,9]
    n = 7
    expected_output = [1,2,3,5,6,7,8]
    assert minimumN(arr1,arr2,n) == expected_output


def run_test_suite():
    test_minimumN()
    test_minimumN_variable_length()
    test_minimumN_r2_greater()

run_test_suite()
