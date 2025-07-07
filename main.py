from typing import List

def generatePalindromes():
    start = 10_000_001
    end =  10_000_0000
    
    for i in range(start,end, 11):
        if isPalindrome(i):
            print(i)
    
        
def isPalindrome(x:int) -> bool:
    if x < 0:
        return False
    if x < 10:
        return True
    num = 0
    k = x
    while k > 0:
        num = num*10 + k%10
        k = k//10
    return num == x


def binary_search(input,x):
    return binary_search_util(input,0,len(input)-1,x)

def binary_search_util(input,i,j,x):
    if i < j:
        mid = (i+j)//2
        print(i,j,mid)
        if x < input[mid]:
            return binary_search_util(input,i,mid,x)
        elif x > input[mid]:
            return binary_search_util(input,mid+1,j,x)
        elif x == input[mid]:
            return True
    else:
        return False
    
input = [1,2,3,4,5]
print(binary_search(input,2))


# Ready 
input = [1,2,3]
target = 5
output = [1,2]

def twoSum(nums:List[int], target:int) -> List[int]:
    n = len(nums)
    if not n:
        return []
    complement_map = dict()
    for i in range(0,n):
        current = nums[i]
        complement = target - current 
        if complement in complement_map:
            return [complement_map[complement], i]
        else:
            complement_map[current] = i
    return []

# Test 
def testTwoSum():
    nums = [1,3,5,7,9]
    target  = 12
    print(twoSum(nums,target))

testTwoSum()