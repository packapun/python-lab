from typing import List

def subsets(nums:List[int]) ->List[List[int]]:
    result:List[int] = []
    def backtrack(start,current_set):
        result.append(current_set[:])
        for i in range(start,len(nums)):
            current_set.append(nums[i])
            backtrack(i+1,current_set)
            current_set.pop()
    
    backtrack(0,[])
    return result 

def print_permutations(s:str):
    def permute(chars,start=0):
        if start == len(chars):
            print(''.join(chars))
        for i in range(start, len(chars)):
            chars[start],chars[i] = chars[i],chars[start]
            permute(chars,i+1)
            chars[start],chars[i] = chars[i],chars[start]
    
    permute(list(s))
    print()
    
    
def test_permutations():
    s = "ABC"
    print_permutations(s)


def test_create_subsets():
    nums = [1,2,3]
    ret = subsets(nums) 
    print(ret)




# test_create_subsets(
test_permutations()